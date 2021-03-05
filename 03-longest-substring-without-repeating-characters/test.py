from main import Solution
import unittest

class TestSubstringMethods(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        self.assertEqual(3, self.s.lengthOfLongestSubstring("pwwkew"))
    
    def test_2(self):
        self.assertEqual(1, self.s.lengthOfLongestSubstring("bbbbb"))
    
    def test_3(self):
        self.assertEqual(3, self.s.lengthOfLongestSubstring("abcabcbb"))

    def test_4(self):
        self.assertEqual(0, self.s.lengthOfLongestSubstring(""))

    def test_5(self):
        self.assertEqual(1, self.s.lengthOfLongestSubstring(" "))
    def test_6(self):
        self.assertEqual(3, self.s.lengthOfLongestSubstring("dvdf"))
    def test_7(self):
        self.assertEqual(4, self.s.lengthOfLongestSubstring("jbpnbwwd"))        
        
if __name__ == '__main__':
    unittest.main()