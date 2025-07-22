"""Module containing mechanism for calculating standard deviation between datasets.
"""

import os
import numpy as np

from inflammation import models, views


def data_analysis(data_source):
    """function to analyze and plot the data"""
    daily_standard_deviation = compute_standard_deviation_by_day(data_source)
    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    return daily_standard_deviation
   # views.visualize(graph_data)

def compute_standard_deviation_by_day(data_source):
    """Calculates the standard deviation by day between datasets.
    Works out the mean inflammation value for each day across all datasets."""

    data= data_source.load_inflammation_data()
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation
