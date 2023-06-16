from .transform import Transform

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
        print(arg,self.anchor,self.mult,self.transp,(arg - self.anchor) * (self.mult - 1) + self.transp)
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
