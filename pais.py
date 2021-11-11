from unittest import TestCase, main




from collections import defaultdict

def binary_search(arr, c, i, j):
    if i + 1 == j:
        return False
    m = (i + j) // 2
    if c == arr[m]:
        return True
    if c > arr[m]:
        return binary_search(arr, c, m, j)
    else:
        return binary_search(arr, c, i, m)
        
def solution(k, arr):
    arr.sort()
    count = 0
    for a in arr:
        if binary_search(arr, a + k, 0, len(arr)):
            count += 1
    return count
    





class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(1, [1,2,3,4]),3)
        self.assertEqual(solution(2,  [1, 5, 3, 4, 2]),3)




        
        
if __name__ == "__main__":
    main()