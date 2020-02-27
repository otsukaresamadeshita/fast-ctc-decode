#!/usr/env/bin python3

import numpy as np
from unittest import TestCase, main
from fast_ctc_decode import beam_search


class Tests(TestCase):

    def setUp(self):
        self.beam_size = 5
        self.alphabet = "NACGT"
        self.beam_cut_threshold = 0.1
        self.probs = self.get_random_data()

    def get_random_data(self, samples=100):
        return np.random.rand(samples, len(self.alphabet)).astype(np.float32)

    def test_beam_search(self):
        """ simple beam search test with the canonical alphabet"""
        seq, path = beam_search(self.probs, self.alphabet, self.beam_size, self.beam_cut_threshold)
        self.assertEqual(len(seq), len(path))
        self.assertEqual(len(set(seq)), len(self.alphabet) - 1)

    def test_beam_search_alphabet(self):
        """ simple beam search test with different alphabet"""
        seq, path = beam_search(self.probs, "NRUST", self.beam_size, self.beam_cut_threshold)
        self.assertEqual(len(seq), len(path))
        self.assertEqual(len(set(seq)), len(self.alphabet) - 1)

    def test_beam_search_short_alphabet(self):
        """ simple beam search test with short alphabet"""
        alphabet = "NAG"
        seq, path = beam_search(self.probs, alphabet, self.beam_size, self.beam_cut_threshold)
        self.assertEqual(len(seq), len(path))
        self.assertEqual(len(set(seq)), len(alphabet) - 1)

    def test_beam_search_long_alphabet(self):
        """ simple beam search test with long alphabet"""
        self.alphabet = "NABCDEFGHIJK"
        self.probs = self.get_random_data(10000)
        seq, path = beam_search(self.probs, self.alphabet, self.beam_size, self.beam_cut_threshold)
        self.assertEqual(len(seq), len(path))
        self.assertEqual(len(set(seq)), len(self.alphabet) - 1)

    def test_beam_search_path(self):
        """ simple beam search with path"""
        w = 5000
        x = np.zeros((w, len(self.alphabet)), np.float32)
        x[:, 0] = 0.5  # set stay prob

        # emit a base evenly spaced along w
        emit = np.arange(0, w, len(self.alphabet) - 1)
        for base, pos in enumerate(emit):
            x[pos, base % 4 + 1] = 1.0

        seq, path = beam_search(x, self.alphabet, self.beam_size, self.beam_cut_threshold)
        np.testing.assert_array_equal(emit, path)
        self.assertEqual(len(seq), len(path))


if __name__ == '__main__':
    main()
