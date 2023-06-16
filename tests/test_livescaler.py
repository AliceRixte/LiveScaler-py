# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import numpy as np

import livescaler.livescaler as ls


class TestLivescaler(unittest.TestCase):

    def test_affine(self) : 
        aff = ls.StdAffine.iii
        assert aff.eval(4) == -5
    
    def test_periodic(self) :
        diff4 = ls.Periodic(np.array([0,1,2,3]),1)
        inv4 = ls.Periodic(np.array([3,2,1,0]),3)
        comp = diff4 >> inv4
        assert comp.anchor == 3
        assert all(comp.period == np.array([5,5,1,1]))
        rescomp = comp.eval(np.array([0,1,2,3]))
        assert all(rescomp == np.array([1,6,7,4]))
        
        #self.assertEqual(rescomp, np.array([1,6,7,4]))


if __name__ == '__main__':
    unittest.main()