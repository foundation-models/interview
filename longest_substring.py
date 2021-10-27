from typing import DefaultDict
from unittest import TestCase, main


    
        

def longest_substring(s):
    last_indices = {}
    start = 0
    longest = 0
    index = 0
    while index < len(s):
        if s[index] in last_indices.keys():
            start = max(start, last_indices[s[index]])
            longest = max(index-start, longest)
        last_indices[s[index]] = index
        index += 1
    longest = max(index-start-1 , longest)
    return len(s) if longest == 0 else longest


class TestSolution(TestCase):
    
    def test_find_word_in_matrix(self):
        self.assertEqual(longest_substring( s = "abcabcbb"), 3)
        self.assertEqual(longest_substring( s = "bbbbb"), 1)
        self.assertEqual(longest_substring( s = "pwwkew"), 3)
        self.assertEqual(longest_substring( s = ""), 0)
        self.assertEqual(longest_substring( s = "aab"), 2)
        self.assertEqual(longest_substring( s = "aabbc"), 2)
        self.assertEqual(longest_substring( s = "aabbcc"), 2)
        self.assertEqual(longest_substring( s = "A"), 1)
        self.assertEqual(longest_substring( s = "abcabcbb"), 3)
        self.assertEqual(longest_substring( s = "abcbdefcbb"), 5)
        self.assertEqual(longest_substring( s = "abcbdefcdefghijba"), 10)



if __name__ == "__main__":
    main()