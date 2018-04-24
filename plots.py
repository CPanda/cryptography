"""
This contains the methods for showing Frequency Analysis and other plots.
"""
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
def freq_analysis(text):
    labels, values = zip(*Counter(['A', 'B', 'A', 'C', 'A', 'A']).items())

    indexes = np.arange(len(labels))
    width = 1

    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    return(plt)