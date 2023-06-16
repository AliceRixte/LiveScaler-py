from abc import ABC, abstractmethod

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