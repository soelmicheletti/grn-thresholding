import numpy as np

class HardThr:
    def __init__(
            self,
            thr,
            return_unweighted = True
    ) -> None:
        self._thr = thr
        self._return_unweighted = return_unweighted

    def __call__(self, G):
        if not isinstance(G, np.ndarray):
            raise ValueError(
                "G has to be a numpy array!"
            )
        G = G.copy()
        G[((G <= np.abs(self._thr)) & (G >= 0))] = 0
        G[((G >= -np.abs(self._thr)) & (G <= 0))] = 0
        if self._return_unweighted:
            G[G > 0] = 1
            G[G < 0] = -1
        return G