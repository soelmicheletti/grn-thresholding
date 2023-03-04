from grn_thresholding import *
import numpy as np
import pandas as pd
import unittest

class homogeneous_thresholding_tests(unittest.TestCase):
    def test_input(self):
        with self.assertRaises(ValueError):
            model = HomogeneousThr(degree = 3, axis = -1)
        with self.assertRaises(ValueError):
            model = HomogeneousThr(degree = 3, axis = 0)
            model(pd.DataFrame(np.random.rand(4, 2)))
        with self.assertRaises(ValueError):
            model = HomogeneousThr(degree = 3, axis = 0)
            model(np.random.normal(0, 1, 53))

    def test_rows(self):
        G = np.asarray([[1, 2, 8], [4, 3, 9], [11, 30, -5]])
        model = HomogeneousThr(degree = 1, axis = 0)
        assert (model(G) == np.asarray([[0, 0, 8], [0, 0, 9], [0, 30, 0]])).all()
        model = HomogeneousThr(degree=0, axis = 0)
        assert (model(G) == 0).all()

    def test_cols(self):
        G = np.asarray([[1, 2, 8], [4, 3, 9], [11, 30, -5]])
        model = HomogeneousThr(degree=1, axis=1)
        assert (model(G) == np.asarray([[0, 0, 0], [0, 0, 9], [11, 30, 0]])).all()
