"""Module containing mock tests to check whether the anaylsis codes are working"""

from unittest.mock import Mock

def test_analyse_data_mock_source():
    """testing with mock data"""
    from inflammation.compute_data import analyse_data
    data_source = Mock()
    data_source.load_inflammation_data.return_value = [[[0, 2, 0]],
                                                     [[0, 1, 0]]]
    analyse_data(data_source)
