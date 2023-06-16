"""! @brief Defines the affine transformation class"""
##
# @file affine.py
#
# @brief Defines the affine transformation class
#
# @section description_affine Description
# Defines the base class and some standard instances of affine transforms
# - Affine (base class)
# - StdAffine
#
# @section author_sensors Author(s)
# - Created by Alice Rixte on 06/16/2023.
# - Modified by Alice Rixte on 06/16/2023.
#
# Copyright (c) Alice Rixte.  All rights reserved.

from .transform import Transform

class Affine(Transform): 
    """! The Affine class allows to declare affine transformations. For more informations about affine transformations, see section 2.3 of this paper https://jim2023.sciencesconf.org/data/pages/3_4_RIXTE.pdf (in french)."""
    def __init__(self, mult, transp, anchor = 0, base = 12)  : 
        """! The Affine initializer
        @param mult The multiplicator coefficient of the affine transform
        @param transp The transposition parameter of the affine transform
        @return  An affine transformation.
        """
        super().__init__(anchor, base)
        self.mult = mult
        self.transp = transp

    def eval_diff(self,arg) : 
        """! Evaluates f(x) - x, where f is this affine transform 
        
        @param arg The argument given to the affine transform. This can be eather a number or a numpy array."""
        return (arg - self.anchor) * (self.mult - 1) + self.transp
    
    def __rshift__(self,other) : 
        """! Combine two affine transforms. Notice that this is *not* the composition of two affine transformations.
         
        @param other A second affine transform to be combined with this one """
        newmult = self.mult * other.mult
        newtransp = other.transp + self.transp
        return Affine(newmult, newtransp)
    
    def __str__(self) : 
        return f"[mult : {self.mult}, transp : {self.transp}, anchor : {self.anchor}, base : {self.base}]"

class StdAffine : 
    """! StdAffine defines some of the most used affine transforms."""
    I = Affine(1,0)
    i = Affine(-1,-5)
    II = Affine(1,2)
    ii = Affine(-1,-3)
    III =  Affine(1,4)
    iii = Affine(-1,-1)
    IV = Affine(1,5)
    iv = Affine(-1,0)
    V = Affine(1,7)
    v = Affine(-1,2)
    VI = Affine(1,9)
    vi = Affine(-1,4)
    VII = Affine(1,11)
    vii = Affine(-1,6)
