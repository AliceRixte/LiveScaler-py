# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import numpy as np

from livescaler import StdAffine, Periodic, FoldInterval


class TestLivescaler(unittest.TestCase):

    def test_interval_default(self) : 
        interval = FoldInterval(12.0,-4.5, 7.5)
        assert interval.descend == -4.5
        assert interval.ascend == 7.5
        assert interval.fold(-4.5) == -4.5
        assert interval.fold(7.5) == -4.5

        assert all(interval.fold(np.array([12.0, -7.0, -36.0]))
             ==  np.array([0.0, 5.0,  0.0]))

    def test_interval_positive(self) : 
        interval = FoldInterval(12.5,50.5, 60.2)
        assert interval.fold(12.0) == 49.5
        assert interval.descend == 49.1
        assert interval.ascend == 61.6
        assert interval.fold(61.6) == 49.1
        assert interval.fold(49.1) == 49.1

        assert all(interval.fold(np.array([60.4, 49.6, 80.0]))
             ==  np.array([60.4,49.6, 55.0]))

    def test_interval_negative(self) : 
        interval = FoldInterval(12.0,-70.0, -30.0)
        assert interval.descend == -74.0
        assert interval.ascend == -26.0
        assert interval.fold(-74.0) == -74.0
        assert interval.fold(-26.0) == -74.0

        assert all(interval.fold(np.array([-72.0, -33.0, -55.0, 12.0, -94.0]))
             ==  np.array([-72.0, -33.0, -55.0 , -36.0, -46.0]))

    def test_affine(self) : 
        aff = StdAffine.iii
        assert aff.eval(4) == 7
        aff.anchor = 4
        assert aff.eval(4) == 3
    
    def test_periodic(self) :
        diff4 = Periodic(np.array([0,1,2,3]),1)
        inv4 = Periodic(np.array([3,2,1,0]),3)
        comp = diff4 >> inv4
        assert comp.anchor == 3
        assert all(comp.period == np.array([5,5,1,1]))
        rescomp = comp.eval(np.array([0,1,2,3]))
        assert all(rescomp == np.array([1,6,7,4]))


if __name__ == '__main__':
    unittest.main()