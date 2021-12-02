from unittest import main, TestCase

def solution():
    return 1

class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 1)

if __name__ == "__main__":
    main()