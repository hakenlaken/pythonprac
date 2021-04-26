# solveSquare()
import unittest
from main import solveSquare as solveSquare1
from main_1 import solveSquare as solveSquare2


class test_solveSquare(unittest.TestCase):
    """test for solveSquare()"""

    def test1_2_solveSquare1(self):
        self.assertEqual(solveSquare1(1, 2, 1), (-1.0, -1.0))

    def test1_1_solveSquare1(self):
        self.assertEqual(solveSquare1(1, 3, 2), (-2.0, -1.0))

    def test1_3_solveSquare1(self):
        self.assertEqual(solveSquare1(10, 1, 10), None)

    def test2_2_solveSquare2(self):
        self.assertEqual(solveSquare2(2, 3, 1.125), (-0.75, -0.75))

    def test2_1_solveSquare2(self):
        self.assertEqual(solveSquare2(2, 3, 1), (-1.0, -0.5))

    def test2_3_solveSquare2(self):
        self.assertEqual(solveSquare2(2, 3, 1.1), (-0.8618033988749892, -0.6381966011250108))

    # def test_3_solveSquare(self):
    #    with self.assertRaises(TypeError):
    #        solveSquare("asd", "asdas", 2)
