from grn_thresholding import *
import numpy as np
import pandas as pd
import unittest

class top_edges_tests(unittest.TestCase):
    def test_input(self):
        with self.assertRaises(ValueError):
            model = BimodalThr([1, 2], [1, 2, 3])

    def test(self):
        data = np.zeros(200)
        data[0:100] = np.random.normal(0, 1, 100)
        data[100:] = np.random.normal(5, 1, 100)
        G=data.reshape((20, 10))
        model=BimodalThr()
        G_thr=model(G)
        for i in range(G.shape[0]):
            for j in range(G.shape[1]):
                if G[i, j] <= 1:
                    assert G_thr[i, j]==0
                if G[i, j] >= 4:
                    assert G_thr[i, j]==1