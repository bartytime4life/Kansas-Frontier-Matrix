#!/usr/bin/env python3
"""Derive the memory-bounded hosted Qwen3-0.6B INT8 model from the pinned upstream files.

Run on an operator PC (never on the host) with onnx==1.23.2 and numpy==2.2.6:

  python3 -I scripts/derive-hosted-qwen.py UPSTREAM_DIR OUTPUT_DIR

UPSTREAM_DIR holds the files of onnx-community/Qwen3-0.6B-ONNX at revision
58ca03a5e7b354b480b1a82b34bde8dc7b854cc0 (config.json, generation_config.json,
tokenizer.json, tokenizer_config.json, onnx/model_int8.onnx). Every input is
checked against its pinned SHA-256 before use. The output is byte-for-byte
reproducible and is what the hosted manifest pins.

Two changes, no new weights and no retraining:
1. Weights move to onnx/model_int8.onnx_data, so the loader can drop its copy
   of the file once onnxruntime-web holds the weights.
2. The tied output layer no longer transposes and dequantizes the whole
   151,936 x 1,024 embedding table on every token (about 780 MB of scratch
   memory per step). It reads 8 pre-transposed uint8 vocabulary slices with the
   same scale and zero point, dequantizes and multiplies one slice at a time and
   concatenates the logits. Greedy output was identical in local comparison.
"""
import hashlib
import json
import os
import shutil
import sys

import numpy as np
import onnx
from onnx import helper, numpy_helper

UPSTREAM_ID = 'onnx-community/Qwen3-0.6B-ONNX'
UPSTREAM_REVISION = '58ca03a5e7b354b480b1a82b34bde8dc7b854cc0'
UPSTREAM = {
    'config.json': '8a04114ba59cc42b47d804d35d1d5c61d746ae4634f41f796768c6e302d39b9e',
    'generation_config.json': '9e9e031ae8bca36eefcdcdd0b35d83c61baa01e31d68d5f5a961c9ca1a4b95bf',
    'tokenizer.json': 'e7a95fce95bf5b0946d0ddb3f9d7caa030b7e850bbe92b0edb26bcf563e9f3d5',
    'tokenizer_config.json': '7c5194eecfd95a4dcbd6b4b502af785d2541fd65a388d1cae7ad43693c67b802',
    'onnx/model_int8.onnx': 'd93222c672992a398eeea3a4a1ca025738efd9a18ba5f1691419ff8ae23a8e75',
}
SLICES = 8
EMBEDDING = 'model.embed_tokens.weight_quantized'
SCALE = 'model.embed_tokens.weight_scale'
ZERO_POINT = 'model.embed_tokens.weight_zero_point'
HIDDEN = '/model/layers.28/final_norm_layernorm/output_0'
REPLACED = ('Transpose_610', 'model.embed_tokens.weight_transposed_DequantizeLinear', '/lm_head/MatMul')
DATA_FILE = 'model_int8.onnx_data'

README = f"""---
license: apache-2.0
base_model: {UPSTREAM_ID}
library_name: onnxruntime
tags:
- onnx
- qwen3
- int8
---

# Qwen3-0.6B INT8 ONNX, memory-bounded output layer (Kansas Frontier Matrix)

Derived from [{UPSTREAM_ID}](https://huggingface.co/{UPSTREAM_ID}) at revision
`{UPSTREAM_REVISION}`, file `onnx/model_int8.onnx`, which is derived from
[Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B). Licensed under
Apache-2.0, as the upstream model is.

**Modified files.** `onnx/model_int8.onnx` and `onnx/{DATA_FILE}` were changed
by `scripts/derive-hosted-qwen.py` in
[bartytime4life/Kansas-Frontier-Matrix](https://github.com/bartytime4life/Kansas-Frontier-Matrix):

- Weights are stored as external data in `onnx/{DATA_FILE}`.
- The tied output layer reads {SLICES} pre-transposed uint8 vocabulary slices of
  the unchanged embedding table, with the unchanged scale and zero point,
  instead of transposing and dequantizing the full table on every token.

No weights were retrained or requantized. The tokenizer and configuration files
are byte-identical copies of the upstream files.
"""


def sha256(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message):
    sys.exit('derive-hosted-qwen: ' + message)


def derive(upstream, output):
    for name, expected in UPSTREAM.items():
        if sha256(os.path.join(upstream, name)) != expected:
            fail(f'{name} does not match the pinned upstream SHA-256')
    if os.path.exists(output):
        fail('output directory already exists; choose a new one')
    os.makedirs(os.path.join(output, 'onnx'))

    model = onnx.load(os.path.join(upstream, 'onnx/model_int8.onnx'))
    graph = model.graph
    names = [node.name for node in graph.node]
    if any(names.count(name) != 1 for name in REPLACED):
        fail('upstream graph does not have the expected output layer')
    weights = {item.name: item for item in graph.initializer}
    table = numpy_helper.to_array(weights[EMBEDDING])
    if table.dtype != np.uint8 or table.shape != (151936, 1024):
        fail('unexpected embedding table')

    nodes = [node for node in graph.node if node.name not in REPLACED]
    bounds = np.linspace(0, table.shape[0], SLICES + 1).astype(int)
    parts = []
    for index in range(SLICES):
        start, end = bounds[index], bounds[index + 1]
        weight = f'lm_head.slice{index}.weight_transposed_quantized'
        graph.initializer.append(numpy_helper.from_array(np.ascontiguousarray(table[start:end].T), weight))
        # Node order keeps each dequantized slice alive only until its MatMul.
        nodes.append(helper.make_node('DequantizeLinear', [weight, SCALE, ZERO_POINT], [f'lm_head.slice{index}.weight'], name=f'lm_head.slice{index}.dequantize'))
        nodes.append(helper.make_node('MatMul', [HIDDEN, f'lm_head.slice{index}.weight'], [f'lm_head.slice{index}.logits'], name=f'lm_head.slice{index}.matmul'))
        parts.append(f'lm_head.slice{index}.logits')
    nodes.append(helper.make_node('Concat', parts, ['logits'], axis=-1, name='lm_head.concat'))
    del graph.node[:]
    graph.node.extend(nodes)
    onnx.save_model(model, os.path.join(output, 'onnx/model_int8.onnx'), save_as_external_data=True,
                    all_tensors_to_one_file=True, location=DATA_FILE, size_threshold=1024)

    for name in UPSTREAM:
        if not name.startswith('onnx/'):
            shutil.copyfile(os.path.join(upstream, name), os.path.join(output, name))
    with open(os.path.join(output, 'README.md'), 'w', encoding='utf-8', newline='\n') as handle:
        handle.write(README)

    files = ['README.md', 'config.json', 'generation_config.json', 'tokenizer.json', 'tokenizer_config.json',
             'onnx/model_int8.onnx', 'onnx/' + DATA_FILE]
    print(json.dumps([{'path': name, 'size': os.path.getsize(os.path.join(output, name)),
                       'sha256': sha256(os.path.join(output, name))} for name in files], indent=2))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        fail('usage: derive-hosted-qwen.py UPSTREAM_DIR OUTPUT_DIR')
    derive(sys.argv[1], sys.argv[2])
