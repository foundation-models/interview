from unittest import TestCase, main
from collections import defaultdict
from collections import Counter

# https://youtu.be/OM5hC6rOIM8
        
def riddle(temp):
    result = []
    while(len(temp) > 0):
        result.append(max(temp))
        for i in range(len(temp) -1):
            temp[i] = min(temp[i], temp[i+1])
        temp.pop()     
    return result
            



class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(riddle([2, 6, 1, 12]),[12, 2, 1, 1])
        self.assertEqual(riddle([1, 2, 3, 5, 1, 13, 3]),[13, 3, 2, 1, 1, 1, 1])
        self.assertEqual(riddle([3,5, 4, 7, 6, 2]),[7, 6, 4, 4, 3, 2])


        
if __name__ == "__main__":
    main()