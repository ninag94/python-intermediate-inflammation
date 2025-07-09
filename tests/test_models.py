"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean
from inflammation.models import daily_max
from inflammation.models import daily_min

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_zeros():
    """tests whether the daily_max functions works if the input is only zeros"""
    test_input = np.array([[0,0],
                           [0,0],
                           [0,0]])
    test_result = np.array([0,0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_general():
    """tests whether the daily_max functions works if the input is random numbers"""
    test_input = np.array([[7,4],
                           [3,6],
                           [2,3]])
    test_result = np.array([7,6])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_same_numbers():
    """tests whether the daily_max functions works if the input is the same number"""
    test_input = np.array([[7,7],
                           [7,7],
                           [7,7]])
    test_result = np.array([7,7])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_min_zeros():
    """tests whether the daily_min function works if the input is only zeros"""
    test_input = np.array([[0,0],
                           [0,0],
                           [0,0]])
    test_result = np.array([0,0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_general():
    """tests whether the daily_min functions works if the input is random numbers"""
    test_input = np.array([[7,4],
                           [3,6],
                           [2,3]])
    test_result = np.array([2,3])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_same_numbers():
    """tests whether the daily_min functions works if the input is the same number"""
    test_input = np.array([[7,7],
                           [7,7],
                           [7,7]])
    test_result = np.array([7,7])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)
