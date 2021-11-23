from unittest import TestCase, main
from collections import defaultdict
from collections import Counter

        
def solution(n):
    z = str(bin(n))[2:]
    n = len(z)
    result = ""
    if n < 32:
        result += "1"*(32-n)
    for ch in z:
        result += str(1 - int(ch))
    return 

class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(2147483647),2147483648)
        self.assertEqual(solution(1),4294967294)
        self.assertEqual(solution(0),4294967295)




        
if __name__ == "__main__":
    main()