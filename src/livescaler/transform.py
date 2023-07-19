"""! @brief Defines the meta class Transform of all LiveScaler transformations"""
##
# @file transform.py
#
# @brief Defines the transform metaclass
#
# @section description_affine Description
# Defines the transform metaclass. Classes using this class are
# - Affine 
# - Periodic
# - Hybrid
#
# @section author_sensors Author(s)
# - Created by Alice Rixte on 06/16/2023.
# - Modified by Alice Rixte on 06/16/2023.
#
# Copyright (c) Alice Rixte.  All rights reserved.

from .interval import FoldInterval
from abc import ABC, abstractmethod
import math

class Transform(ABC):
    """! This is the meta class of all transformations in LiveScaler. 
    
    This allows to separate  interval foldbacks and base/anchor preoccupation from the core of the transform, which must be implemented in subclasses via the eval_diff function and the composition >> """
    def __init__(self, anchor = 0, base = 12, max_descend_diff = -4.5, max_ascend_diff = 7.5) : 
        self.anchor = anchor
        self._fold_interval = FoldInterval(base, max_descend_diff, max_ascend_diff )

    @abstractmethod
    def eval_diff(self,arg) : 
        """! Evaluates f(x) - x, where f is this transform 
        
        @param arg The argument given to the transform. This can be eather a number or a numpy array."""
        pass

    def eval(self, arg) : 
        """! Evaluates f(x), where f is this transform 
        
        @param arg The argument given to the transform. This can be eather a number or a numpy array."""
        return arg + self._fold_interval.fold(self.eval_diff(arg))

    @abstractmethod
    def __rshift__(self, other) : 
        """! Combine two transforms. This behaves like reversed function composition : for a function f and a function g, g(f(x)) will be (f >> g)(x)
         
        @param other A second transform to be combined with this one """
        pass

    def __str__(self) : 
        return f"[anchor : {self.anchor}, base : {self.base}]"
    
       
