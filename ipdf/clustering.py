import logging
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth

from ipdf.memory_tournament import load_tournament_results
from ipdf.constants import DEFAULT_QUANTILE


LOGGER = logging.getLogger(__name__)


def transform_data(scores):
    """Convert list of dicts to a list of lists"""
    transformed_data = [list(col) for col in zip(*[d.values() for d in scores])]
    return transformed_data[0], transformed_data[1]


def clusterify_data(scores, quantile=DEFAULT_QUANTILE):
    names, values = transform_data(scores)

    X = np.array(list(zip(values, np.zeros(len(values)))), dtype=np.int)
    bandwidth = estimate_bandwidth(X, quantile=quantile)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    clusters = [None] * n_clusters_
    for i, label in enumerate(labels):
        LOGGER.info(f'adding strategy {names[i]} to cluster {label}')
        if not clusters[int(label)]:
            clusters[int(label)] = []
        clusters[int(label)].append(scores[i])
    return clusters


if __name__ == '__main__':
    _, _, results = load_tournament_results()
    clusters = clusterify_data(results)
    number_of_clusters = len(clusters)
    print(number_of_clusters)
