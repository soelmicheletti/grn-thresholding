from grn_thresholding import *
import numpy as np
import pandas as pd
import unittest

class hard_thresholding_tests(unittest.TestCase):
    def test_input(self):
        model = HardThr(thr = .5)
        with self.assertRaises(ValueError):
            model(pd.DataFrame(np.random.rand(4, 3)))

    def test(self):
        G = np.asarray([[1, 2, 8], [4, 3, 9], [11, 30, -5]])
        G_thr = np.asarray([[0, 0, 8], [0, 0, 9], [11, 30, 0]])
        model = HardThr(thr = 7, return_unweighted=False)
        assert (model(G) == G_thr).all()
        model = HardThr(thr = 8, return_unweighted=False)
        assert model(G)[0, 2] == 0
        model = HardThr(thr = 7)
        G_thr[G_thr != 0] = 1
        assert(model(G) == G_thr).all()