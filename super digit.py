from unittest import TestCase, main
from collections import defaultdict
from collections import Counter

        
def solution(n,k):
    
    def sub(m):
        if m < 10:
            return m
        sum = 0
        for c in str(m):
            sum += sub(int(c))
        return sub(sum)            
    
    return sub(sub(n)*k)



class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(123,3),9)
        self.assertEqual(solution(9875,4),8)
        self.assertEqual(solution(148,3),3)
        self.assertEqual(solution(123,3),9)


        
if __name__ == "__main__":
    main()