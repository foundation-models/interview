from unittest import TestCase, main




from collections import defaultdict
from math import sqrt

def downToZero_wrong(n):
    
    def xx(nn, count):
        y = []
        for x in range(nn-1, 1, -1):
            if nn % x == 0:
                y.append(x)
        print(y)
        if len(y) == 0:
            count += nn
            return count
        count += 1
        return xx(y[(len(y) - 1) // 2], count)
    
    return xx(n, 0)

from collections import deque
def downToZero(n):
    memo = set()
    count = 0
    q = deque([[n, count]])
    while q:
        n, count = q.popleft()
        if n <= 1:
            if n == 1:
                count += 1
            break
        if n-1 not in memo:
            memo.add(n-1)
            q.append([n-1, count+1])
        for x in range(int(sqrt(n)), 1, -1):
            if n%x == 0:
                y = max(n//x, x)
                if y not in memo:
                    memo.add(y)
                    q.append([y, count + 1])
    return count
                    
        
def solution(n):
    return downToZero(n)

    





class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(3),3)
        self.assertEqual(solution(4),3)
        self.assertEqual(solution(10),5)
        self.assertEqual(solution(7),5)
        self.assertEqual(solution(24),5)
        self.assertEqual(solution(24*7),6)




        
        
if __name__ == "__main__":
    main()