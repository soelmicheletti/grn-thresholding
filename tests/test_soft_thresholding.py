from grn_thresholding import *
import numpy as np
import pandas as pd
import unittest

class soft_thresholding_tests(unittest.TestCase):
    def test_input(self):
        model = SoftThr(beta = .5)
        with self.assertRaises(ValueError):
            model(pd.DataFrame(np.random.rand(4, 3)))

    def test(self):
        G = np.asarray([[1, 2, 8], [4, 3, 9], [11, 30, 5]])
        G_thr = G ** .5
        model = SoftThr(beta = .5)
        assert (model(G) == G_thr).all()