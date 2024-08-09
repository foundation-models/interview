from typing import List
from unittest import main, TestCase

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        x = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = x
        return nums
 
        
if __name__ == "__main__":
    x = Solution()
    # assert(x.merge([], 0, [], 0) == [])
    # assert(x.merge([0], 1, [1], 1) == [1])
    assert(x.rotate([1,2,3,4,5,6,7], 3) == [1,2,2,3,5,6])


