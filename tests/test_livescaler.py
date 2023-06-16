# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from livescaler.livescaler import add


class TestLivescaler(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,3), 5)


if __name__ == '__main__':
    unittest.main()