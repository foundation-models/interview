from unittest import TestCase, main
from collections import defaultdict
from collections import Counter

        
def solution(n):

    def sub(n, result):
        if n == -2 or n == -1:
            return 0
        if n == 1 or n == 0:
            return 1
        if result.get(n, 0) != 0:
            return result[n]
        answer = sub(n - 3, result) + sub (n - 2, result) + sub (n - 1, result)
        result[n] = answer
        return answer
        
    
    return sub(n, {})




class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(1),1)
        self.assertEqual(solution(2),2)
        self.assertEqual(solution(3),4)
        self.assertEqual(solution(5),13)
        self.assertEqual(solution(7),44)





        
        
if __name__ == "__main__":
    main()