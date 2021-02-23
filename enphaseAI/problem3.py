import argparse
import os

import numpy as np
from sklearn import mixture
from sklearn.cluster import DBSCAN

from enphaseAI.utils.constants import DATA_DIR
from enphaseAI.utils.gaussian_generator import generate_multivariate_gaussian
from enphaseAI.utils.matplotlib_plotter import basic_plot


def main(args):
    eps = args.eps
    min_samples = args.min_samples

    # Q1 ------------------------------------------------------------------------------
    if not(os.path.exists(os.path.join(DATA_DIR, "sample_data_generated.npy"))):
        samples = (25, 25, 25, 25)
        data = generate_multivariate_gaussian(samples)
        np.save(os.path.join(DATA_DIR, "sample_data_generated.npy"), data)
    else:
        data = np.load(os.path.join(DATA_DIR, "sample_data_generated.npy"))

    # Q2 ------------------------------------------------------------------------------
    labels = np.zeros(data.shape[0])
    basic_plot("generated_clusters.png", data, labels)
    
    # Q3 ------------------------------------------------------------------------------
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = dbscan.fit(data)
    basic_plot("generated_clusters_fit.png", data, clusters.labels_)
    # In this figure, we can see the 4 clusters we generated, being clustered correctly
    # Being pretty well separated, it was easy to adjust the parameters to fit all the points
    # Without having some being labelled as noise (-1) or miss classified.

    # Q4 ------------------------------------------------------------------------------
    data_test = np.load(os.path.join(DATA_DIR, "sample_data.npy"))
    labels = np.zeros(data_test.shape[0])
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = dbscan.fit(data_test)
    basic_plot("test_clusters_fit.png", data_test, clusters.labels_)
    # We pretty much observe the same thing as the last figure. We can see that the parameters
    # we chose for the generated data still suits the test data.
    
    # Q5 ------------------------------------------------------------------------------
    # A)
    # Since the clusters were well seperated, it has been possible to cluster all the points
    # to their respective clusters (with very high probability). For this particular task,
    # if there were missclassified points it's probably because of a bad choice of hyperparameters.
    # If we had chosen clusters that were closer and with a subtancial overlab, it would
    # have been probable that points are missclassified
    #
    # B)
    # Like discussed before, the clustering with the test data is with very high probability
    # perfect. I had to tune the esp value (which is the maximum distance for two samples to be
    # considered in the neighborhood of the other) to reach perfect clustering. If the
    # clustering wouldn't have been perfect I would have tuned the other hyperparameters.
    #
    # C)
    # For this task DBSCAN is a very good choice for clustering because it finds regions
    # of high density and expands the region to delimit the cluster. Another good model
    # that would have probably work better is a GMM (gaussian mixture model), especially because
    # it is what i used to generate the data points. Also since GMM is a parametric model
    # (compared to DBSCAN) it has more capacity because we directly optimize for the parameters
    # Since we "know" the clusters and they are pretty obvious, a Kmeans would have probably
    # worked as good as the other algorithm.
    # Could even use diagonal covariance (what i uses to generate the data)
    gmm_labels = mixture.GaussianMixture(n_components=4, covariance_type='full').fit_predict(data_test)
    basic_plot("test_clusters_gmm.png", data_test, gmm_labels)
    #
    # D)
    # DBSCAN belong to the fully unsupervised learning class since we don't have any labels
    # for the training of our model.


    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e",
                        "--eps",
                        default=4.,
                        type=float,
                        help="Eps parameter of DBSCAN algorithm")
    parser.add_argument("-s",
                        "--min_samples",
                        default=5,
                        type=int,
                        help="min_smaples from DBSCAN algorithm")
    
    args = parser.parse_args()

    main(args)
