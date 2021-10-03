
from unittest import TestCase, main

class Solution(object):
    def twoSum(self, nums, target):
      required = {}
      for i in range(len(nums)):
         if target - nums[i] in required:
            return [required[target - nums[i]],i]
         else:
            required[nums[i]]=i


class TestPractice(TestCase):
    
    def test_two_sum(self):
        input_list = [2,8,12,15]
        ob1 = Solution()
        print(ob1.twoSum(input_list, 10)  )
              
if __name__ == "__main__":
    main()