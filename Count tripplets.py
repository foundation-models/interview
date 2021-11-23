from unittest import TestCase, main
from collections import defaultdict
from collections import Counter

        
def solution(arr,k):
    result = defaultdict(int)
    x = []
    for i in range(len(arr)-1):
        if arr[i]*k in arr:
            result[arr[i]] += 1
    if len(result.keys()) > 1:
        sum = 1
        for value in result.values():
            sum *= value
    return sum
    # fact = 1
    # for i in range(1,sum+1):
    #     fact = fact * i
    # return fact // 2

class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([1, 2, 2, 4],2),2)
        self.assertEqual(solution([1, 3, 9, 9, 27, 81],3),6)
        self.assertEqual(solution([1, 5, 5, 25, 125],5),4)



        
if __name__ == "__main__":
    main()