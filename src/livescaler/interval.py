"""! @brief Defines the fold interval class."""
##
# @file interval.py
#
# @brief Fold interval class.
#
# @section description_affine Description
#  Defines the interval class that represents a musical interval for LiveScaler.
#
# @section author_sensors Author(s)
# - Created by Alice Rixte on 07/19/2023.
# - Modified by Alice Rixte on 07/19/2023.
#
# Copyright (c) Alice Rixte.  All rights reserved.

from math import ceil

class FoldInterval :
  """! A fold interval to restraint the maximal interval between a note and the result of its transformation"""

  def __init__(self, base = 12.0, max_descend_diff = -4.5, max_ascend_diff= 7.5):
    self._base = base
    self._descend = 0
    self._ascend = 0
    self._span = 0
    self.setBounds(max_descend_diff, max_ascend_diff)
    

  """! This sets the minimal and maximal intervals between a note and it's transformation. If the interval length `max_diff - min_diff ` is not a multiple of the base, the resulting FoldInterval will be bigger : its length will be rounded to the next base multiple and the initial interval will be centered in that bigger interval.

  @param max_descend_diff The maximal descending interval allowed between a note and its transformed version. In most use cases this should be negative.
  @param max_ascend_diff The maximal ascending interval allowed between a note and its transformed version. In most use cases this should be positive."""

  def setBounds(self, max_descend_diff, max_ascend_diff) : 
    if max_ascend_diff < max_descend_diff : 
      max_descend_diff, max_ascend_diff = max_descend_diff, max_ascend_diff
    interval = max_ascend_diff - max_descend_diff
    mult_base = ceil(interval / self.base) * self.base

    # Centering the new bigger interval
    margin = (mult_base - interval) / 2.0
    self._descend = max_descend_diff - margin
    self._ascend = max_ascend_diff + margin
    self._span = mult_base


  """! The effective maximal descend interval. In most cases this should be negative. This can be lower than expected when the interval given to FoldInterval is not a multiple of the base."""
  @property
  def descend(self) : 
    return self._descend

  """! The effective maximal ascend interval. In most cases this should be positive. This can be higher than expected when the interval given to FoldInterval is not a multiple of the base."""
  @property
  def ascend(self) : 
    return self._ascend
  
  """! The base used to fold the interval"""
  @property
  def base(self) : 
    return self._base
  
  @base.setter
  def base(self, value) : 
    self._base = value
  
  """! Folds the interval between a note and its transform.
    
  @param diff Interval between a note and its transform."""
  def fold(self, diff) : 
    return self._descend + (diff - self._descend) % self._span