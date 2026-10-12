from __future__ import annotations

import base64
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / 'tools/validators/validate_taxonomic_concept_lineage.py'
SPEC = importlib.util.spec_from_file_location('validate_taxonomic_concept_lineage', MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

VALID_VECTOR = 'eNrdWG1v2zYQ/p5fYfhzFVPvkr8FibcZSOMg9dp1wyBQ1DFRK4kCRblNi/73kXqx9eI4TpCtwQAjCMgjefc8j+6O/H4ymUxZ+AmICMR9DtP5ZLrGX1nG0pics4xALi7jDPAtXGPyGcT0jVpRkDtIcbABXsQsU4v0U3SK6sm8MgziSI2LerN7Lal3mRd5Eje73OHiLsg5o3FSHfyZphqNv4qSg/apYJm20ZvjciCBslZWxR02bGdueDpYEQU7skzfpA6yogiDAT5yPcMKAYeG5+ly3DU95HsRgGcQ27FChDxMfKPeOcMpBGUhHSvk3n/Jocnke/VXTlbjTRzKUKsG5iyJqsWVTcFKTiCIoCA8zgXjAQfaBDOfzerpWYvCDI9WclYHvz77Y3W1ers8D85+X/+2ulmuP45sMyziTevR2Xx1ebEzqSIpBI+zWzV7ASmbVMfuTHAp7hgv7uJcWmRlkmxnOM4+V9hKoGMJxZs+BIXAolQATaVfvy6vzi53FoIDFilkoh/4dniGZwbS0W7BBidxFFDOUmWt5jSky98aoXn1+3NoK1htaViabmimvjbMue3LX8cSNnEEmcIT6I7Kaqp2qDXYcaF4bKz+7sDYQCxdj8W9lCcUwDegIBe8hMrux5ujhJLBF41l8DrEcrX4oB+hlknP4RdQzNn5+eJ6vbh4omIMuw/dUDVy/hjV9Hx+hkZaCv91nYgv7NXoxDhGJz2Hf6pOep78RJ0oP56pk5NmSV0uA1IX3j0lqZnpFletGXvhujSQxXmv2JCYkzKtt5YNQBDFsoCKTnUmIUZOaLumQzF1XLBl3XVD29EBgy8Ltg2uaxFbd7Eb+TrCtmU6PuiGYxJCw8jqSIuo4CCqq3QbxUPl+EG5vaaq0zK2VcveZHGI6pevLEO6++XiUb4dZPrIN6iLPNli+aYNjm4BpohSSw9J6Oum7YIHruX4vkt9TG2b2qFPXepRx3sK36PYj+b8P8wFDVG92vEsll+2Luxh2XgCy5GNLIp0B3mhi70QWablY19+sZZjImr5uguOS4gFoeMhM8KmDnKJCcjCCBHHeyLLvdhfM8vdzD9I6C2/HBKsQN2T09uphpZ203a4vjH1Ja+iDXZb0yMyhGCHF/TTaOtSeyd8d325XAe/3KzedpIfpfLaqPSExePQPwPi+qo4KqkcqntnWLU4D/Zax6Hak9hxqPaW/O9R3QqZg4opTuI6hEh+hcV+PbdTwxeAdrzzBNDpBMcBHMj5k4O5YjLqD0bRdkgbnHr4M5o8pojJPgWMjmelICytNHB9s3q/fLdc9S7VdT+t+sVBJ/8xeLdefDi76fRizQPKEO1meB7Jln1svPflpsmzil8sbQiLYABOLdjF++XF4up8EdzI/xYfZM8+CvAldUkYj2Sl2H4OjoY8Ddlr3Rh9DkWZy8BA+r0VaPNd9i8lQ613gWepRIDIZQVLSlGDRHFSDD+IAnJcgyUNavF3r0tBXAQZE9vOv3fSqB4Xo4tBY9gKdVibGwKH5mVW+S23UXmJJjERD+3cAt86yggpOa9Ia8nZZYIf9cseZxvIcD3ThHyAH7PPz5SXig0CcT640jWDQy20y+qIeKPw5hbIWDIbPi5qVX3HsjEare0IHp3qW8FP4ywvR2ng0TesY14sDtxWT9pOoYb1VqLKB7CK9hE22OUCovaqaKz02ESwh7eAJDhOR5ZRrKQZVqJ+wKTRJY7SWIyPypkU1L08BiflHk+kPFJWbd74/G1kIksg4AIeNsjLUJ6Bj9tl92krLE9+nPwDmnurgA=='
INVALID_VECTORS = {'invalid_name_string_identity.json': {'payload': 'eNrFV9Fu4jgUfe9XIJ6bkoRAA29dirSVZtqKMp3tjFaR49wUTxM7sh00zKj/vrbjkJCUTrca7UoIId/ja/vcc4/Nz5PBYMjib4BlJHcFDOeD4Rp9Z5TlBC8YxVDID4QCeoRbhJ9ADk/1DIE3kKNoC1wQRvUk78w9c6tgYYARSfS4rJLtnKzKMqcoBwezLEOFgGrCBolNVHCWksxs4CnNnZR8lyUH55tg1Nl6dtkCcKTRGiU2yJ9M50HsBaGbjL0wTr0UT904xoGL40ns43M/nM58H4fjiY9RkAYzb5KCBzAOz4NZ6IIXjqvMeldRKdQGhcr9VQ0NBj/NtwqacXses30zMEdYswOJg0wOAxWs5BiiBATmpJCMRxxSe6b5aFSFRzUpo/5MzioO1hd/3VzffLxaRBef1n/erK7WDz0sRZJs641dzD3XbSDmQEJyQh9NlCacFeyR0cEjcMQTQhosKuWGcbEhhYbeE5kj2kQ5ok+Gb0U+UfScHtIiJJKlMGssFsvb9fKyQUgOSOZA5SEL++ERGvmuP2kmbFFGkijlLNdoHXNcT33Wrjs3ny9drGQKScss24/DliRANZWQNsU0oWr5GtAug8X83eLPcqu2SeROyRME8C1oriUvweCeT98kFLGjjO5yJ363TuLfp5M/5v7bdKIacksoJopmcUwrH1B+9g6l3D1c31w/fPwXQom1UIJXhBL8J0KJ3yuUEzul8sMIV876gtfYSNs9HTs2/50+0/GOxYF5YMJxmVeplb9HCVG+KFumG2N3Np2M3UniJ8oFPZiOU8+N/SAJMUzOZ9MwdsMgPD9P4hDiNEXjiRegwPUQckOYteRcm2hlvvUpfuGyR4X2P/mHLZDT+Ein6nVVOWRIM2ryViEOOkgygiqq1YlEjTiURh3q3qz1eO0z3b7rn+N1egdHzKsn/eZU3QW6uu1NZaXELIfm2ug6jG6ljsc9RHfr5eeLVeuCsY+GLiN2eJ5AzvrgF18tVle6BkhhMEugc6a7m0+rxTK6vlhf3S+jq8u76Ha1vFuu7ls33mDvbdHy/upyea0mrNSv5WcF6pHwDqUdqqWfUsd5otoJSdsBU8cNHXey9vxeB4iyUFSAOuledrYBDxqCg2EsNsXQltYuFcvVTrCaJlhWyorWFGWi63sCClTRqwCVpNt3T0RERJnc22idpVqqZ1qiZ7MWWEuy62C25l14Sc3GVRptyWlG1DP4SOa6BPVOGcYl56Z8dZkax3+uHsLqBgWKqog98ysFGh8WaMhLXQ4MpOhci3awUcVh4w/tmbhtC3uXMpaNuq9xx5ggUvdHb26rS9wzb98lQ0KLstfyv3zYHbnPT2qzrAh7VHzxDmGy/jcSNcaAdR5ToLZIXqhIhDNE8h4yIVp1sdHrEYhVHEpyIvtLFUxJZaeWQVn5wk5U4XNmkts9/+hB1E0ASMBxQFHGag30tixN12ouT55P/gH8OhwC', 'codes': ['NAME_STRING_IDENTITY_COLLAPSE', 'SCHEMA_INVALID']}, 'invalid_unresolved_usage_accepted.json': {'payload': 'eNrFV11v4jgUfe+vQDw3JSF8lbcuRdpKHago7WxntIr8cVM8TeLIdtAwo/73tR2ngaR0utVoV0II+R5f2+eee2x+nnQ6XY6/AVGR2uXQnXa6a/SdZzxlZMYzArm6ZhmgR7hB5AlU99TMkGQDKYq2ICTjmZkUnPlnfhnMLTBi1IyrMtnOS8os0yITIHmyBeohYtKXkzZIbqJc8JgldhNPcerF7LsqBHjfJM+8beCWzoFEBm1QcoP6w9F0EOLROMaAyTntU8BhGNAgHI9JPJgMxygESukED2gcYjwKzwdDBH6IhiOK+yM8wKMyc4ZSiAqpNyl17q96qNP5ab910I67MxmgZwem5RHMWWwOC5W8EAQiCpIIlisuIgGxO9O01yvDvYqYXnum4CUH64u/lovlp6tZdHG3/nO5ulo/tLAZUmxbbexiGvh+DbEHkkqw7NFGMyp4zh951nkEgQRlrMaiQm24kBuWG+g9UynK6qhA2ZPlW5PPND2nh7RIhVQh7Rqz2fxmPb+sEUoAUilk6pCFl+Ee6vX9/rCesEUJo1EseGrQJub5gf6sfX9qP1+aWMU1MiuS5GUctoxCZqiEuC6mDZXLV4D9MjjM33v8OW71NpnaaXmCBKGVqzMqUYDFPZ++Syhyl/Fsl3r4wzrBv08nf0z779OJbsgtywjTNMtjWrlG6dkHlHK3WM1vl9f3/0or2Ghl8IZWBv+JVvBHtXLippS2GJHSYF+xGxfZN1HPjU1/p9U07GN24B+ECVKkZWpt8xFl2hrVnu9i4p+PhqE/1K6rjTCAURgHPu4P6ITAcHw+mmB/MpiMxxRPAMcxCofBAA38ACF/Aud7iq58tPTf6hS/MNqjWvufLMQVyKutpFH1qqoCEmQYtXnLkAATZAlDJdX6RLJCHEqjCjUv2Gq8sppm67XP8Ta9nSP+1ZJ+farmAk3dtqbyQhGeQn1zNE3GtFLD5h6i2/X888Vqzzfcu6HJiBueUkh5G/zq48XpytQAaQzhFBpnul3erWbzaHGxvrqfR1eXt9GNNrL5at/IDOxhsVw8fIrm91eX84WesNK/5p81qEXCB5R2qJZ2ShMXVLcTUq4DRp4/8fzhOui3OkAWuaYC9ElfZOca8KAhBFjGsC2GsbT9UvFU74RE9mlXqJLWGCWy6XsSclTSqwGlpPevn4jJKOPqxUYPVmp5lmy5rANWimwamCt5E14/SY0jxwnTj+EjmasKVBvlhBRC2OpVVaoN/7l8Dus7FDJURtyR36hPeFifrihMNQiwvHErusFaFId933VnEq4r3FXKedJrvsk964FIXx+tuXtN4p8FL03SZVletDr+l0+7I9f5SeWVJWGPmi/RIExV/0mi2heIyWMLZJXmdvZKRSKSIJa2kJQZ0WEr1yMQpzhEU6baS+VcS2Wnl0FJ8cpOdOFTbpO7Pf9oQfRFAEjCcUBeYL0Gel+WumkNlyfPJ/8ADHofxQ==', 'codes': ['UNRESOLVED_USAGE_ACCEPTED']}, 'invalid_relation_endpoint.json': {'payload': 'eNrVWG1v2zYQ/p5fYfhzVJOWRFn+FiTeZiBLgtRr1w2DQFHHRq0kChTlNiv630fqxbYkx3GCbM0AIwjII3n3PI/ujvx2MhqNRfgJmArUfQ7j+Wi8ol9FJtKYnYuMQa4u4wzoR7ih7DOo8alZUbA7SGmwBlnEIjOL8Bv0BtWTeWUYxJEZV/Vm91ZS7zIPaWRJSKgyCyv7O1rcBbkUPE6q8z/z1OLxV1VKsD4VIrPWuDk1BxYYa2NV3NGpS+YhxjZhxPcYInhK/AhHBPtTFvqRHSHi+gy4HXrOzCdkhn0IsYO9GWA7dCgjpHE5oykEZaH9K/Tef+qh0ehb9VdPVuNNOMbQqgbmIomqxZVNIUrJIIigYDLOlZCBBN4EM59M6ulJC8aEDlZKUQe/Ovv9+ur61+V5cPbb6pfr2+Xqw8A20+CtW4/O5teXF1uTKpJCyTj7aGYvIBWj6titCS3VnZDFXZxri6xMks2MpNnnClsNdKyhOO1CUCiqSgPQWPv18/Lq7HJroSRQlUKmuoFvhid0MkUYbResaRJHAZciNdZmzkJY/1YIzavfH31bJWrLqWPhqWXj1dSeu77+7VjCOo4gM3gC31JZTdUOtQZbLgyPjdVfOzA2EGvXY3Wv5QkFyDUYyJUsobL7fnqUUDL4YokMXodYrhbv8RFqGXUcfgHFnJ2fL25Wi4snKmbqdqHrq0bPH6Oajs/P0EhL4b+uE/VFvBqdTI/RScfhH6qTjic/UCfGj2fq5KRZUlfNgNX1d09JamZ2a6zVjL1wXerJ4rxTbFgsWZnWW+tyHkSxLqBqpzqzkCISup5NOOXEA9cJkRe6BAMF37F9FzzPYS72qBf5GFHXsYkPuo7bjPEwcnakxUxwENVVuo3ioXL8oNxeU9VpGduoZW+yOET1y1eWPt3dcvEo3wTZPvKn3EMz4oS+7QLBDlCOOHdwqJsybLsezMBziO973Kfcdbkb+tzjM05mT+F7EPvRnP+HuaAhqlM7nsXyy9aFPSxPn8By5CKHI0zQLPToLESO7fjU11+sQ2zEHR97QDzGHAjJDNkRtTHoJTYghyLEyOyJLHdif80s72b+XkJv+W1vPntyejvV0NJu2g7PizyJVVfyJtpguzU/IkMocXhBGheFqfKnA7fa6+Hbm8vlKvjp9vrXnQTIub5BGk1R9Tj8z4C5Cn5YViVUV9CwanMe7LeOQ7Yjs+OQ7Sx5DNlugfoforoRswQTU5zEdQiR/hKL/Zpup/qPAe14DX2/GxwGcCDvjw7mi9GgRxhEu0Na79TDn9LoMUWM9ilgcLwoFRNppYGb2+t3y7fL687Fuu6pTc/Y6+Y/BG9Xi/dntzv9WPOI0ke7GZ5Hum0fGu99xGlyreGXahsmIuiBUwt28W55sbg6XwS3+r/Fe923DwJ8SV0yISNdLTafA7HQzELuCk8Hn0NR5jow0H5vBNp8l92LSV/ru8CLVCPA9LJCJKWqQeI0KfofRAE5rcHSBrX4d69MQVwEmVCb7r9z0qAmF4PLQWPYCrVfnxsC++ZlVvmttzF5iScxUw/t3ALfOioYK6WsSGvJ2WaC7/UjnxRryGg904R8gB+7y89YloYNBnHeu9Y1g30ttMvqiGSj8OYmKEQy6b8zWlWNp7o5GqzdETx6gzeCH8dZXg7SwKPvWMe8Why4sZ603UIN60eNquzBqtr32GCbC5jZq6Kx0mMTwR7eApbQOB1YRrGRZliJ+gGTRpc0SmM1PCoXWlD3+hialHs80fJIRbV54/PfAxNdAoEW8LBBXob6DHrcLttP22B58v3kHwtjrwE=', 'codes': ['RELATION_CONCEPT_UNRESOLVED']}, 'invalid_spec_hash.json': {'payload': 'eNrFV9Fu4jgUfecrEM9NSSi0lDeWIi3SDFTAdLY7GlmOcwOeJnZkO2jYUf99bcchkJROtzvarVCFfI+v7XPPPTY/Wu12h4ffgCik9hl0Ru3OGn/njKeUTDgjkKkPlAHewD0mT6A6F2aGJFtIMdqBkJQzMym49C/9IphZIKKRGVdFsr2XFFlGIY68LZbbAmu+oUzwmCZ27ac49WL6XeUCvG+SM28XuBUzIMjO0yi5xb3B9Qj+5V+RmeEUUC713qTO/UUPtds/7H8dtOPuKAbo2YERJoYYiDxsc1io5LkggCKQRNBMcYEExO5Mo263CHdLPrrNmYIXHKzHfyzmi4+zCRp/Wv++WM7Wjw0sw4ruyo2NR4HvVxB7IKkEZRsbZZHgGd9w1t6AwCKitMLiXG25kFuaGegDVSlmVVRg9mT51uRTTc/FKS1SYZVLu8ZkMr1fT+8qhBKAVQpMnbJwGO7ibs/vDaoJO5zQCMWCpwZtYp4f6M/a90f282cdq7hGsjxJDuOwoxEwQyXEVTFtqFi+BByXwWG+HvHnuNXbpGqv5QkSxA4M10rkYHHPF28SitwzzvapF75bJ+Gv08lvo97bdKIbckcZoZpmeU4rH3B6+Q6lrB7ni/njx38glNAIpf+KUPr/iVDC9wql5aYUVohIYaoveI2LHBun58ZGv9Jnat4xOTEPQgXJ0yK1tnYUUe2L6sh0Q+LfXg+u/EHUi7QLBnB9FQd+2OtHQwKDm9vrYegP+8ObmygcQhjH+GoQ9HHfDzD2h3B7JOfSRAvzLU/xE5c9K7T/yT9cgbzKR2pVL6sqIMGGUZu3CAkwQZpQXFCtTyRLxKk0ylD9Ui3HS5+p913zHK/T2z5jXg3pV6eqL1DXbWMqzxXhKVTXRt1hTCvVPO4RrdbTz+Pl0QXjHg11RtzwKIKUN8EvPlicrkwNsMYQHkHtTKvFp+Vkiubj9exhimZ3K3S/nK6my4ejG6998DY0fZjdTed6wlJ/m37WoAYJ71DaqVqaKU1cRLqdsHIdcO35Q88frINeowNknmkqQJ/0IDvXgCcNIcAyFtpiGEs7LhVP9U6IniZ5kquC1hgnsu57EjJc0KsBhaSP7x5EJWJcHWz0ZKWGZ8mGyzpgqci6gbmS1+E5s/vWaYwjxwnVD+AzmcsKlBvlhORC2OqVVaoM/7l4AusLFBguIu7Ir9Tn6rQ+HZGbahCgWe1WdIOVKE77vuPOJFxXuKuU86Rbf4d71gOxvj4ac4+axL8MDk3SoSzLGx3/03fdmeu8VXplQdhG8yVqhKnydwiqfIGYPLZAVmluZy9UBJEE07SBjKgRXWjlegbiFIejlKrmUhnXUtnrZXCSv7ATXfiU2+Ruz381IPoiACzhPCDLQ70GfluWqmkNl63n1t+lOCGv', 'codes': ['SPEC_HASH_MISMATCH']}}


def decode_vector(encoded: str) -> str:
    return zlib.decompress(base64.b64decode(encoded)).decode("utf-8")


class TaxonomicConceptLineageTests(unittest.TestCase):
    def write_vector(self, directory: str, name: str, encoded: str) -> Path:
        path = Path(directory) / name
        path.write_text(decode_vector(encoded), encoding="utf-8")
        return path

    def test_valid_vector_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_vector(directory, "valid.json", VALID_VECTOR)
            self.assertTrue(validator.validate_packet(path).ok)

    def test_invalid_vectors_match_reviewed_codes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for name, item in INVALID_VECTORS.items():
                with self.subTest(path=name):
                    path = self.write_vector(directory, name, item["payload"])
                    result = validator.validate_packet(path)
                    self.assertEqual(sorted({finding.code for finding in result.findings}), item["codes"])

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"object_type":"x","object_type":"y"}', encoding="utf-8")
            result = validator.validate_packet(path)
            self.assertIn("JSON_DUPLICATE_KEY", {finding.code for finding in result.findings})
            self.assertTrue(result.error)

    def test_cli_does_not_echo_candidate_values(self) -> None:
        marker = 'UNIQUE_TAXON_ECHO_SENTINEL'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps({"marker": marker}), encoding="utf-8")
            run = subprocess.run([sys.executable, str(MODULE_PATH), str(path)], cwd=REPO_ROOT, capture_output=True, text=True, check=False)
            self.assertNotEqual(run.returncode, 0)
            self.assertNotIn(marker, run.stdout)
            self.assertNotIn(marker, run.stderr)

    def test_hash_is_deterministic(self) -> None:
        candidate = json.loads(decode_vector(VALID_VECTOR))
        expected = validator.canonical_spec_hash(candidate)
        self.assertEqual(candidate["spec_hash"], expected)
        self.assertEqual(expected, validator.canonical_spec_hash(candidate))

    def test_schema_is_valid(self) -> None:
        validator._schema_findings(json.loads(decode_vector(VALID_VECTOR)))


if __name__ == "__main__":
    unittest.main()
