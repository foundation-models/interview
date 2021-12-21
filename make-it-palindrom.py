
from unittest import main, TestCase

def isPalindrome(s):
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    start = 0
    while(not isPalindrome(s[start:])):
        start += 1
    print(start)
    return s + s[:start][::-1]

class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(make_palindrome("abbb"), "abbba")
        self.assertEqual(make_palindrome("abc"), "abcba")
        self.assertEqual(make_palindrome("abcddc"), "abcddcba")
        self.assertEqual(make_palindrome("abcddc"), "abcddcba")
        self.assertEqual(make_palindrome("abcdc"), "abcdcba")
        self.assertEqual(make_palindrome("abcdce"), "abcdcecdcba")
        self.assertEqual(make_palindrome("Race"), "RacecaR")


if __name__ == "__main__":
    main()

