from unittest import TestCase
from unittest import TestCase, main

def can_jump(nums):
    n = len(nums)
    for i in range(n-1,-1,-1):
        if i + nums[i] >= n:
            n = i
        if n == 0:
            return True
    return False

class TestSolution(TestCase):
    
    def test_jump_game(self):
        self.assertTrue(can_jump([2,3,1,1,4]))
        self.assertFalse(can_jump([3,2,1,0,4]))
        self.assertTrue(can_jump([2,3,0,0,4]))

if __name__ == "__main__":
    main()