"""! @brief Defines the periodic transformation class"""
##
# @file periodic.py
#
# @brief Defines the periodic transformation class
#
# @section description_periodic Description
# Defines the base class and some standard instances of periodic transforms
# - Periodic (base class)
# - StdPeriodic
#
# @section author_sensors Author(s)
# - Created by Alice Rixte on 06/16/2023.
# - Modified by Alice Rixte on 06/16/2023.
#
# Copyright (c) Alice Rixte.  All rights reserved.

import numpy as np

from .transform import Transform

class Periodic(Transform) : 
    """! The Periodic class allows to declare periodic with respect to an intervam transformations. For more informations about these transformations, see section 2.2 of this paper https://jim2023.sciencesconf.org/data/pages/3_4_RIXTE.pdf (in french)."""
    def __init__(self, period, anchor = 0) : 
        """! The Affine initializer
        @param period A vector of the size of the base asigning to each value of the interval upon which the function is periodic the difference value. The period vector corresponds to f(x) - x where x belongs to [0, base-1], with base being the length of period.
        """
        super().__init__(anchor, len(period))
        self.period = period


    def eval_diff(self, arg) : 
        """! Evaluates x - f(x), where f is this periodic transform 
        
        @param arg The argument given to the periodic transform. This can be eather a number or a numpy array."""
        return self.period[(arg + self.anchor) % self.base]
    
    def __rshift__(self, other): 
        """! Combine two periodic transforms. Notice that this is *not* the composition of two periodic transformations.
         
        @param other A second periodic transform to be combined with this one """
        anchor_shift = np.roll(self.period , other.anchor - self.anchor)
        newperiod =  other.period + anchor_shift
        return Periodic(newperiod,other.anchor)
    
    def __str__(self) : 
        return f"[period : {self.period}, anchor : {self.anchor}, base : {self.base}]"


class StdPeriodic :
    """! StdPeriodic defines some of the most used affine transforms."""
    Id = Periodic(np.zeros(12))