![Alt text](/wallpaper.jpg?raw=true "Title")
# GRN-Thresholding

[![master](https://github.com/soelmicheletti/grn-thresholding/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/soelmicheletti/grn-thresholding/actions/workflows/python-app.yml)[![PyPI - Python Version](https://img.shields.io/pypi/v/grn-thresholding?style=flat&colorA=0f0f0f&colorB=0f0f0f)](https://pypi.org/project/grn-thresholding/)

Implementation of a collection of methods to threshold weighted (un)directed graphs, such that only the edges with largest (absolute) weight are retained. This methods have been designed for specific applications in the context of Gene Regulatory Networks, but can be applied in a variety of scenarios. 

## Install

```bash
$ pip install grn-thresholding
```


## Usage

```python
import numpy as np
from grn_thresholding import *

model = HardThr(thr=0.5)
mu = 0
sigma = 1
dim = (50, 50)
X = np.random.normal(mu, sigma, dim)
thresholded_network = model(X)
print(thresholded_network)
```

The example above, given a randomly generated network, retains only the edges with absolute value greater equal 0.5. Using the parameter `return_unweighted`, the user can specify whether she wants to map the non-zero weights to {-1, 1}. 

The following is a short overview of all available methods. 

```python
"""
Only keeps edges with weight larger than a user-specified threshold. 

:param thr: only weights with absolute value larger than thr are retained
:param return_unweighted: if set to True, non-zero entries are mapped to {-1, 1}
"""
model = HardThr(thr, return_unweighted=True)

"""
Performs soft thresholding similarly as WGCNA, by elevating the network to the power of a parameter beta (which usually is between 0 and 1). 

:param beta: strength of soft thresholding
"""
model = SoftThr(beta=1)


"""
Keep the edges with largest absolute value, such that all nodes have the same in/out degree. 

:param degree: final degree of the edges
:param axis=0: set it to zero for homogeneous out-degree, and to one for homogneous in-degree
"""
model = HomogeneousThr(degree, axis=0)


"""
Keep only the edges with largest absolute value. 

:param k: final number of non-zero edges
:param ratio: ratio of retained non-zero edges. Exactly one parameter in {k, ratio} must be provided by the user. 
:param return_unweighted: if set to True, non-zero entries are mapped to {-1, 1}
"""
model = TopEdges(k=None, ratio=None, return_unweighted=True)

"""
Thresholds the graphs by picking the threshold maximizing the F1 score. 
 
:param return_unweighted: if set to True, non-zero entries are mapped to {-1, 1}
"""
model = MaxF1Score(return_unweighted=True)
thresholded_graph=model(G, G_gt)

"""
Threshold the graph to maximize the separation between two gaussian distribution. Useful if the distribution of the weights is bimodal, as can happen in GRN inferred from a motif prior. 

:param means: initial guess for the means of both distributions. 
:param standard_deviations: initial guess for the standard deviations of both distributions. 
"""
model = BimodalThr(means=None, sd=None)
```
