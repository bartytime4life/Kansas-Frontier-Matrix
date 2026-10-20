#!/usr/bin/env python3
"""Encode complete native map-frame sequences with Pillow and external FFmpeg."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

from PIL import Image

CATEGORIES = (
    'weather', 'science', 'government', 'rivers',
    'underground', 'history', 'transport', 'farming',
)
TOUR_IDS = tuple(f'{category}-{number}' for category in CATEGORIES for number in (1, 2))
FRAME_COUNT = 120
PLAYBACK_FPS = 24
ENCODED_FRAMES = 168
DIMENSIONS = (1280, 720)
HASH_METHOD = 'SHA256 of ASCII SHA256 hex digest lines in frame-index order, with final newline'
ENCODER = {
    'codec': 'libvpx-vp9', 'crf': 30, 'cpuUsed': 5, 'pixelFormat': 'yuv420p',
    'filter': 'tpad=start_mode=clone:start_duration=1:stop_mode=clone:stop_duration=1,setsar=1',
    'inputFps': PLAYBACK_FPS, 'outputFrames': ENCODED_FRAMES,
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inspect_frames(raw, identity, metadata):
    """Bind every native input frame to the byte evidence written by the recorder."""
    hashes = []
    byte_count = 0
    require(len(metadata['frameBytes']) == FRAME_COUNT, f'{identity}: missing frame byte evidence')
    for index in range(FRAME_COUNT):
        frame = raw / f'{identity}.frame-{index:03d}.jpg'
        data = frame.read_bytes()
        require(len(data) == metadata['frameBytes'][index], f'{frame.name}: capture byte mismatch')
        with Image.open(frame) as image:
            require(image.size == DIMENSIONS, f'{frame.name}: not native HD output')
        hashes.append(digest(data))
        byte_count += len(data)
    require(len(set(hashes)) > 100, f'{identity}: frozen or duplicate input sequence')
    aggregate = digest(('\n'.join(hashes) + '\n').encode('ascii'))
    return hashes, aggregate, byte_count


def encode(ffmpeg, raw, identity, video, poster):
    subprocess.run([
        ffmpeg, '-y', '-hide_banner', '-loglevel', 'error',
        '-framerate', str(PLAYBACK_FPS), '-start_number', '0',
        '-i', str(raw / f'{identity}.frame-%03d.jpg'),
        '-vf', ENCODER['filter'], '-frames:v', str(ENCODED_FRAMES), '-an',
        '-c:v', ENCODER['codec'], '-crf', str(ENCODER['crf']), '-b:v', '0',
        '-cpu-used', str(ENCODER['cpuUsed']), '-row-mt', '1', '-threads', '2',
        '-pix_fmt', ENCODER['pixelFormat'], str(video),
    ], check=True)
    subprocess.run([
        ffmpeg, '-y', '-hide_banner', '-loglevel', 'error', '-ss', '1.5',
        '-i', str(video), '-frames:v', '1', '-q:v', '2', str(poster),
    ], check=True)


def preserve_native_proof(metadata):
    # Early captures ran the same native-pixel and no-upscaling guards, but did
    # not retain exact source dimensions. Keep that invariant explicit instead
    # of fabricating a measured viewport after the fact.
    if 'nativeMapViewport' not in metadata:
        metadata['nativeResolutionProof'] = {
            'minimumPixelWidth': 1280, 'minimumPixelHeight': 720, 'noUpscaling': True,
            'verificationMethod': (
                'Exporter checked native buffer size and rejected scale greater than one '
                'for every frame; exact source dimensions were not retained.'
            ),
        }
        metadata['configuredViewport'] = {
            'width': 1280, 'height': 720, 'pixelRatio': 1,
            'evidence': 'Explicit fixed map-host configuration, not a retained runtime measurement.',
        }


def package_tour(args, identity, metadata):
    require(metadata['id'] == identity, f'{identity}: mismatched capture identity')
    require(metadata['kind'] == 'rendered-software-tour', f'{identity}: wrong capture kind')
    require(metadata['frameCount'] == FRAME_COUNT, f'{identity}: incomplete native frames')
    hashes, aggregate, byte_count = inspect_frames(args.raw, identity, metadata)
    evidence = args.output / f'{identity}.capture.json'
    video = args.output / f'{identity}.webm'
    poster = args.output / f'{identity}.jpg'
    previous = json.loads(evidence.read_text()) if evidence.exists() else {}
    if previous.get('inputFramesSha256') != aggregate or not video.exists() or not poster.exists():
        print(f'Encoding {identity}: {FRAME_COUNT} native HD frames', flush=True)
        encode(args.ffmpeg, args.raw, identity, video, poster)
    preserve_native_proof(metadata)
    metadata.update(
        uniqueInputFrameCount=len(set(hashes)), inputFramesSha256=aggregate,
        inputFrameHashes=hashes, inputFrameBytes=byte_count, inputHashMethod=HASH_METHOD,
        encodedFrameCount=ENCODED_FRAMES, playbackFps=PLAYBACK_FPS,
        packagedDurationSeconds=ENCODED_FRAMES / PLAYBACK_FPS, encoder=ENCODER,
    )
    evidence.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
    assets = [{
        'path': f'/welcome/demos/{asset.name}', 'bytes': asset.stat().st_size,
        'sha256': digest(asset.read_bytes()),
    } for asset in (video, poster)]
    print(f'{identity}: packaged {video.stat().st_size:,} bytes', flush=True)
    return metadata, assets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--ffmpeg', default='ffmpeg')
    parser.add_argument('--allow-incomplete', action='store_true')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    captures, files = [], []
    for identity in TOUR_IDS:
        path = args.raw / f'{identity}.json'
        metadata = json.loads(path.read_text()) if path.exists() else None
        if not metadata or metadata.get('state') != 'complete':
            if args.allow_incomplete:
                continue
            raise ValueError(f'{identity}: complete source capture required')
        capture, assets = package_tour(args, identity, metadata)
        captures.append(capture)
        files.extend(assets)
    used_bytes = sum(asset['bytes'] for asset in files)
    if len(captures) == len(TOUR_IDS):
        manifest = {'usedBytes': used_bytes, 'files': files, 'captures': captures}
        (args.output / 'runtime-assets.json').write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
        )
    print(f'Packaged {len(captures)}/{len(TOUR_IDS)} tours; {used_bytes:,} bytes', flush=True)


if __name__ == '__main__':
    main()
