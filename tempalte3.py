from unittest import TestCase, main
def solution(s, k):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if (s[i] + s[j]) % k == 0:
                count += 1

    return count

class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution([1, 7, 2, 4], 3), 3)
        
if __name__ == "__main__":
    main()