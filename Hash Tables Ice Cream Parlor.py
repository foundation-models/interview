from unittest import TestCase, main




from collections import defaultdict


def binary_search(arr, c, i, j):
    if i+1 == j:
        return False
    middle = (i + j) // 2
    if arr[middle] == c:
        return True
    elif arr[middle] < c:
        return binary_search(arr, c, middle, j)
    else:
        return binary_search(arr, c, i, middle)
    


def solution(cost, money):
    # Write your code here
    # Write your code here
    rindex = defaultdict(list)
    for i, c in enumerate(cost):
        rindex[c].append(i+1)
    cost.sort()
    for c in cost:
        if binary_search(cost, money - c, 0, len(cost)):
            if c != (money - c):
                print(rindex[c][0], rindex[money - c][0])  if rindex[c][0] < rindex[money - c][0] else print(rindex[money - c][0], rindex[c][0])
                return rindex[c][0], rindex[money - c][0] if rindex[c][0] < rindex[money - c][0] else (rindex[money - c][0], rindex[c][0])
            elif len(rindex[c]) > 1:
                rindex[c].sort()
                print(rindex[c][0], rindex[c][1])
                return rindex[c][0], rindex[c][1]




class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([1, 4, 5, 3, 2],4),(1,4))
        self.assertEqual(solution([2, 2, 4, 3],4),(1,2))
        self.assertEqual(solution([4,3,2,5,7],8),(2,4))
        self.assertEqual(solution([7,2,5,4,11],12),(1,3))



        
        
if __name__ == "__main__":
    main()