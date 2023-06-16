import numpy as np

from .transform import Transform

class Periodic(Transform) : 
    def __init__(self, period, anchor = 0) : 
        super().__init__(anchor, len(period))
        self.period = period


    def eval_diff(self, arg) : 
        return self.period[(arg + self.anchor) % self.base]
    
    def __rshift__(self, other): 
        anchor_shift = np.roll(self.period , other.anchor - self.anchor)
        newperiod =  other.period + anchor_shift
        return Periodic(newperiod,other.anchor)
    
    def __str__(self) : 
        return f"[period : {self.period}, anchor : {self.anchor}, base : {self.base}]"

""" diff4 = Periodic(np.array([0,1,2,3]),2)
inv4 = Periodic(np.array([3,2,1,0]),3)
comp = diff4 >> StdAffine.I
print(comp) """