from collections import defaultdict
from typing import Iterator
from unittest import TestCase, main


def my_solution(nums):
    result = {}
    max = None
    count = defaultdict(lambda: 0)
    for index, num in enumerate(nums):
        count[nums[index]] += 1
        max = count[nums[index]] if max is None or max < count[nums[index]] else max

    for key in count.keys():
       if max != count[key]:
           result[key] = max - count[key] 
    return result

class TestMySolution(TestCase):
    
    def test_my_solution(self):
        # write my test case
        self.assertEqual(my_solution([1,1,2]), {2: 1})
        self.assertEqual(my_solution([1, 1, 1, 5, 3, 2, 2]),  {5: 2, 3: 2, 2: 1})

if __name__ == "__main__":
    main()