import mixem
import numpy as np

class BimodalThr:
    def __init__(
            self,
            means = None,
            standard_deviations = None
    ) -> None:
        self._means = means
        self._standard_deviations = standard_deviations
        if self._means is not None and  len(self._means) != 2:
            raise ValueError(
                "The means parameter must be a list of length two!"
            )
        if self._standard_deviations is not None and  len(self._standard_deviations) != 2:
            raise ValueError(
                "The standard_deviations parameter must be a list of length two!"
            )

    def __call__(self, G):
        if not isinstance(G, np.ndarray):
            raise ValueError(
                "G has to be a numpy array!"
            )
        G = G.copy()
        weights = G.flatten()
        if self._means is None:
            self._means=[np.quantile(weights, 1/3), np.quantile(weights, 2/3)]
        if self._standard_deviations is None:
            self._standard_deviations=[1, 1]
        clusters = mixem.em(weights, [mixem.distribution.NormalDistribution(self._means[0], self._standard_deviations[0]),
                            mixem.distribution.NormalDistribution(self._means[1], self._standard_deviations[1])])
        means=[clusters[1][0].mu, clusters[1][1].mu]
        sd=[clusters[1][0].sigma, clusters[1][1].sigma]
        if means[1] < means[0]:
            tmp = means[0]
            means[0]=means[1]
            means[1]=tmp
            tmp=sd[0]
            sd[0]=sd[1]
            sd[1]=tmp
        thr=means[0]+(sd[0] / (sd[0] +sd[1])) * np.abs(means[1] - means[0])
        G[G<thr]=0
        G[G!=0]=1
        return G