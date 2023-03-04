import numpy as np

class SoftThr:
    def __init__(
            self,
            beta = 1
    ) -> None:
        self._beta = beta

    def __call__(self, G):
        if not isinstance(G, np.ndarray):
            raise ValueError(
                "G has to be a numpy array!"
            )
        G = G.copy() ** self._beta
        return G