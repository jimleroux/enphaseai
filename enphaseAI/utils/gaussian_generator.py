from typing import Tuple

import numpy as np


def generate_multivariate_gaussian(samples: Tuple[int, int, int, int]) -> np.ndarray:
    """
    Generates samples from 4 multivariate gaussian (2d). For simplicity we will hardcode
    the mean and covariance of the 4 clusters

    Args:
        samples (Tuple[int, int, int, int]): Tuple containing the number of samples per
                                             clusters
    """

    mu1, sigma1 = [5, 5], [[2, 0], [0, 2]]
    mu2, sigma2 = [5, 20], [[3, 0], [0, 3]]
    mu3, sigma3 = [20, 20], [[2, 0], [0, 2]]
    mu4, sigma4 = [20, 5], [[7, 0], [0, 7]]

    g1 = np.random.multivariate_normal(mu1, sigma1, samples[0])
    g2 = np.random.multivariate_normal(mu2, sigma2, samples[1])
    g3 = np.random.multivariate_normal(mu3, sigma3, samples[2])
    g4 = np.random.multivariate_normal(mu4, sigma4, samples[3])

    data = np.concatenate([g1, g2, g3, g4], axis=0)

    return data
