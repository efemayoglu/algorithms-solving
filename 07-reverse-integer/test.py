import sys
import unittest
from main import Solution

class TestAll(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(321,self.solution.reverse(123))

    def test_2(self):
        self.assertEqual(-543,self.solution.reverse(-345))

    def test_3(self):
        self.assertEqual(-33543,self.solution.reverse(-34533))

    def test_4(self):
        self.assertEqual(0,self.solution.reverse(0))

    def test_5(self):
        self.assertEqual(3241,self.solution.reverse(1423))
    def test_6(self):
        self.assertEqual(-1,self.solution.reverse(-1))

    def test_44(self):
        self.assertEqual(1,self.solution.reverse(1))

    def test_7(self):
        self.assertEqual(-1,self.solution.reverse(-10))

    def test_8(self):
        self.assertEqual(-9,self.solution.reverse(-9))

    def test_9(self):
        self.assertEqual(1,self.solution.reverse(10))

    def test_10(self):
        self.assertEqual(11,self.solution.reverse(11))


    def test_11(self):
        self.assertEqual(5,self.solution.reverse(5))



    def test_12(self):
        self.assertEqual(0,self.solution.reverse(1534236469))


    def test_13(self):
        self.assertEqual(0,self.solution.reverse((-sys.maxsize-2)))

if __name__ == '__main__':
    unittest.main()