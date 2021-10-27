from unittest import TestCase, main

def longestPalindrome(s):
    reversed = s[::-1]

    for candidate_length in range(len(s), 0, -1):
        print(candidate_length)
        candidates = [s[i:j] for i in range(candidate_length) for j in range(i+1,len(s)+1) if (j-i) == candidate_length]
        for candidate in candidates:
            if candidate in reversed:
                return candidate
    return None

class TestSolution(TestCase):

    
    def test_longestPalindrome(self):
        self.assertEqual(longestPalindrome("babad"), "bab")
        self.assertEqual(longestPalindrome("cbbd"), "bb")
        self.assertEqual(longestPalindrome("a"), "a")
        self.assertEqual(longestPalindrome("ac"), "a")
        # self.assertEqual(longestPalindrome("aacabdkacaa"), "aca")

        

if __name__ == "__main__":
    main()