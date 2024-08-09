from typing import List
from unittest import main, TestCase

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        while(nums2):
            print(j, nums2[0], nums1[j])
            if nums2[0] < nums1[j]:
                nums1[j+1:] = nums1[j:-1]
                nums1[j] = nums2.pop(0)
            elif nums1[j] == 0:
                nums1[j:] = nums2
                break
            j += 1  
        print(nums1)
        return nums1     
        
if __name__ == "__main__":
    x = Solution()
    assert(x.merge([], 0, [], 0) == [])
    assert(x.merge([0], 1, [1], 1) == [1])
    assert(x.merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6])


