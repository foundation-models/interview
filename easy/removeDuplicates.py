from typing import List
from unittest import main, TestCase

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while(i < len(nums)):
            j = i +1
            while(j < len(nums)):
                if nums[i] == nums[j]:
                    nums.pop(j)
                else:
                    break
            i += 1
        return len(nums)
        
if __name__ == "__main__":
    x = Solution()
    # assert(x.merge([], 0, [], 0) == [])
    # assert(x.merge([0], 1, [1], 1) == [1])
    assert(x.removeDuplicates([0,0, 1,2,2,3,4]) == 5)


