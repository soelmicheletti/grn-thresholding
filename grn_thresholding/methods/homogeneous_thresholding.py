import numpy as np

class HomogeneousThr:
    def __init__(
            self,
            degree,
            axis = 0
    ) -> None:
        self._degree = degree
        self._axis = axis
        if self._degree < 0:
            raise ValueError(
                "Degree must be non-negative!"
            )
        if axis != 0 and axis != 1:
            raise ValueError(
                "Axis should be set to 0 (to get rows with the same degree) or 1 (to get columns with the same degree"
            )

    def __call__(self, G):
        if not isinstance(G, np.ndarray):
            raise ValueError(
                "G has to be a numpy array!"
            )
        if len(G.shape) != 2:
            raise ValueError(
                "G must be a matrix!"
            )
        G = G.copy()
        if self._axis == 0:
            for i in range(G.shape[0]):
                a = np.abs(G[i, :]).argsort()[::-1].argsort()
                G[i, a >= self._degree] = 0
        else:
            for i in range(G.shape[1]):
                a = np.abs(G[:, i]).argsort()[::-1].argsort()
                G[a >= self._degree, i] = 0
        return G