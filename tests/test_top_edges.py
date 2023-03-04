from grn_thresholding import *
import numpy as np
import unittest

class top_edges_tests(unittest.TestCase):
    def test_input(self):
        with self.assertRaises(ValueError):
            model = TopEdges(k = 10, ratio = .3, return_unweighted=False)
        with self.assertRaises(ValueError):
            model = TopEdges()

    def test_k(self):
        G = np.asarray([[1, 2, 8], [4, 3, 9], [11, 30, -5]])
        G_thr = np.asarray([[0, 0, 8], [0, 0, 9], [11, 30, 0]])
        model = TopEdges(k = 4, return_unweighted=False)
        assert (model(G) == G_thr).all()
        model = TopEdges(k=4)
        G_thr[G_thr != 0] = 1
        assert(model(G) == G_thr).all()

    def test_ratio(self):
        G = np.asarray([[1, 2, 8], [4, 3, 9], [11, 30, -5]])
        G_thr = np.asarray([[0, 0, 0], [0, 0, 9], [11, 30, 0]])
        model = TopEdges(ratio=1/3, return_unweighted=False)
        assert (model(G) == G_thr).all()
        model = TopEdges(ratio=1/3)
        G_thr[G_thr != 0] = 1
        assert (model(G) == G_thr).all()