import unittest
from solve import solve

class TestEq(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solve(5, 2), -0.4)
        self.assertEqual(solve(4, 1), -0.25)

    def test_2(self):
        self.assertEqual(solve(0, 4), None)

