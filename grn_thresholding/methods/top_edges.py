import numpy as np

class TopEdges:
    def __init__(
            self,
            k = None,
            ratio = None,
            return_unweighted = True
    ) -> None:
        self._k = k
        self._ratio = ratio
        if k is None and ratio is None:
            raise ValueError(
                "Please provide either the parameter k (number of edges you want to keep) or the parameter ratio (ratio of edges you want to keep)!"
            )
        if k is not None and ratio is not None:
            raise ValueError(
                "Please don't set both the k and the ratio parameter, pick only one!"
            )
        self._return_unweighted = return_unweighted

    def __call__(self, G):
        if not isinstance(G, np.ndarray):
            raise Exception(
                "G has to be a numpy array!"
            )
        G = G.copy()
        if self._k is not None:
            G[np.abs(G).flatten().argsort()[::-1].argsort().reshape(G.shape) >= self._k] = 0
        else :
            edges = 1
            for i in range(len(G.shape)):
                edges *= G.shape[i]
            G[np.abs(G).flatten().argsort()[::-1].argsort().reshape(G.shape) >= edges * self._ratio] = 0
        if self._return_unweighted:
            G[G > 0] = 1
            G[G < 0] = -1
        return G