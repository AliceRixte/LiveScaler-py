from abc import ABC, abstractmethod
import numpy as np

class Transform(ABC):
    def __init__(self, anchor = 0, base = 12) : 
        self.anchor = anchor
        self.base = base

    @abstractmethod
    def eval_diff(self,arg) : 
        pass

    def eval(self, arg) : 
        return arg + self.eval_diff(arg)

    @abstractmethod
    def __rshift__(self, other) : 
        pass

    def __str__(self) : 
        return f"[anchor : {self.anchor}, base : {self.base}]"

class Affine(Transform): 
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
        return arg * (self.mult - 1) + self.transp
    
    def __rshift__(self,other) : 
        newmult = self.mult * other.mult
        newtransp = other.mult * self.transp + other.transp
        return Affine(newmult, newtransp)
    
    def __and__(self, other) : 
        """! Combine two affine transforms. Notice that this is *not* the composition of two affine transformations, see >> for a proper composition. Contrarily to >>, this operator & is commutative.
         
        @param other A second affine transform to be combined with this one """
        newmult = self.mult * other.mult
        newtransp = other.transp + self.transp
        return Affine(newmult, newtransp)
    
    def __str__(self) : 
        return f"[mult : {self.mult}, transp : {self.transp}, anchor : {self.anchor}, base : {self.base}]"

class StdAffine : 
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


class Periodic(Transform) : 
    def __init__(self, period, anchor = 0) : 
        super().__init__(anchor, len(period))
        self.period = period

    def eval_diff(self, arg) : 
        return self.period[(arg + self.anchor) % self.base]
    
    def __rshift__(self, other):
        if(self.base != other.base) :
            raise ValueError("Can't compose two transformations with different base")
        anchorshift =  other.anchor - self.anchor
        newperiod = np.roll(self.period, anchorshift)  +  other.period
        return Periodic(newperiod,other.anchor)
    
    def __str__(self) : 
        return f"[period : {self.period}, anchor : {self.anchor}, base : {self.base}]"
    

