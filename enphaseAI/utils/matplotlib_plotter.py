import os

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from enphaseAI.utils.constants import FIGURE_DIR


def basic_plot(
    name: str,
    data: np.ndarray,
    labels: np.ndarray,
    xlabel: str = "x",
    ylabel: str = "y"
) -> None:

    plt.style.use("ggplot")
    fig, ax = plt.subplots()

    clusters = set(labels)
    num_ele = data.shape[0]
    num_clusters = len(clusters)

    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(labelsize=15)

    colors = [cm.Set1(lab + 1) for lab in labels]
    for i in range(num_clusters):
        cluster = list(clusters)[i]
        x = data[labels == cluster, 0]
        y = data[labels == cluster, 1]
        scatter = ax.scatter(x, y, color=np.array(colors)[labels == cluster], label=str(int(cluster)))

    plt.tight_layout()
    plt.legend()
    plt.savefig(os.path.join(FIGURE_DIR, name))
    plt.show()
