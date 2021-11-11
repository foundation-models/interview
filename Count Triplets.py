from unittest import TestCase, main
from collections import defaultdict

        
def solution(arr, r):
        count = 0
        dict = {}
        dictPairs = {}

        for i in reversed(arr):
                if i*r in dictPairs:
                        count += dictPairs[i*r]
                if i*r in dict:
                        dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

                dict[i] = dict.get(i, 0) + 1

        return count



class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([1,2,2,4],2),2)
        self.assertEqual(solution([1,5,5,25,125], 5), 4)
        self.assertEqual(solution([1,3,9,9,27,81], 3), 6)





        
        
if __name__ == "__main__":
    main()