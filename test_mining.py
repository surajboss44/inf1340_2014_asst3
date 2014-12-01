#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
from mining import *


def test_goog():
    read_stock_data("GOOG","data/GOOG.json")
    assert six_best_months() == [('2007-12', 693.76), ('2007-11', 676.55), ('2007-10', 637.38), ('2008-01', 599.42),
                                 ('2008-05', 576.29), ('2008-06', 555.34)]
    assert six_worst_months() == [('2004-08', 104.66), ('2004-09', 116.38), ('2004-10', 164.52), ('2004-11', 177.09),
                                  ('2004-12', 181.01), ('2005-03', 181.18)]


def test_tse():
    """
    Correct values calculated from TSE-SO.json
    """
    read_stock_data("TSE-SO", "data/TSE-SO.json")
    assert six_best_months() == [('2007-12', 20.98), ('2007-11', 20.89), ('2013-05', 19.96), ('2013-04', 19.65),
                                 ('2007-10', 19.11), ('2008-02', 18.93)]
    assert six_worst_months() == [('2009-03', 1.74), ('2008-11', 2.08), ('2008-12', 2.25), ('2009-02', 2.41),
                                  ('2009-04', 2.75), ('2009-01', 3.14)]

#
# def test_no_file():
#     """
#     Tests the result if file name is not specified.
#     """
#     with pytest.raises(FileNotFoundError):
#         read_stock_data("GOOG", "")

#
# def test_no_stock_name():
#     """
#     Tests the result if stock name is not specified.
#     """
#     with pytest.raises(ValueError):
#         read_stock_data("", "data/GOOG.json")
