# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

import livescaler.livescaler as ls


class TestLivescaler(unittest.TestCase):

    def test_affine(self) : 
        aff = ls.StdAffine.iii
        self.assertEqual(aff.eval(4), -5)


if __name__ == '__main__':
    unittest.main()