import numpy as np
from sklearn.metrics import auc, f1_score, roc_curve

class MaxF1Score:
    def __init__(
            self,
            return_unweighted=True
    ) -> None:
        self._return_unweighted = return_unweighted
    def __call__(self, G, G_gt):
        if not isinstance(G, np.ndarray):
            raise ValueError(
                "G has to be a numpy array!"
            )
        if not isinstance(G, np.ndarray):
            raise ValueError(
                "Ground truth has to be a numpy array!"
            )
        G = G.copy()
        fpr, tpr, thresholds = roc_curve(G_gt.flatten(), G.flatten())
        best_threshold = thresholds[0]
        best_score = float('inf')
        for thr in thresholds:
            tmp = G.copy()
            tmp[tmp <= thr] = 0
            tmp[tmp != 0] = 1
            score = f1_score(G_gt.flatten(), tmp.flatten())
            if score < best_score:
                best_score = score
                best_threshold = thr
        G[G <= best_threshold] = 0
        if self._return_unweighted:
            G[G != 0] = 1
        return G