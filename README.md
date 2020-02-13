# fast-ctc-decode

![test-fast-ctc-decode](https://github.com/nanoporetech/fast-ctc-decode/workflows/test-fast-ctc-decode/badge.svg) [![PyPI version](https://badge.fury.io/py/fast-ctc-decode.svg)](https://badge.fury.io/py/fast-ctc-decode)

Blitzing fast beam search.

```
$ pip install fast-ctc-decode
```

## Usage

```python
>>> from fast_ctc_decode import beam_search
>>>
>>> beam_size = 5
>>> alphabet = "NACGT"
>>> beam_prune_threshold = 0.1  # < 1 / len(alphabet)
>>> posteriors = np.random.rand(100, len(alphabet)).astype(np.float32)
>>>
>>> beam_search(posteriors, alphabet, beam_size, beam_prune_threshold)
'ACACTCGCAGCGCGATACGACTGATCGAGATATACTCAGTGTACACAGT'
```

## Benchmark

| Implementation       | Time (s) | URL |
| -------------------- | -------- | --- |
| Greedy (Python)      |   0.0022 |     |
| Beam Search (Rust)   |   0.0033 | [nanoporetech/fast-ctc-decode](https://github.com/nanoporetech/fast-ctc-decode.git) |
| Beam Search (C++)    |   0.1034 | [parlance/ctcdecode](https://github.com/parlance/ctcdecode) |
| Beam Search (Python) |   3.3337 | [githubharald/CTCDecoder](https://github.com/githubharald/CTCDecoder) |


## Developer Quickstart

```
$ git clone https://github.com/nanoporetech/fast-ctc-decode.git
$ cd fast-ctc-decode
$ pip install --user maturin
$ make test
```

Note: You'll need a recent [rust](https://www.rust-lang.org/tools/install) compiler on your path to build the project.

## Credits

The original beam search implementation was developed by [@usamec](https://github.com/usamec) for [deepnano-blitz](https://github.com/fmfi-compbio/deepnano-blitz).
