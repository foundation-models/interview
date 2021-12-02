from unittest import TestCase, main
   
def solution(X, Y, s, T):
    t = T - X - Y
    if t > s:
        result = (s + 1)**2
        diff = ((t - s + 1) * (t - s + 2) // 2)
        if diff > result:
            return result
        else:
            return result - diff
    return (t + 1) * (t + 2) // 2

class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(2, 2, 3, 6),6)
        self.assertEqual(solution(2, 2, 3, 12),16)
        self.assertEqual(solution(2, 2, 3, 8),13)

        
if __name__ == "__main__":
    main()