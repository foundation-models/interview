class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def find_index(nums, lower_index, upper_index, target):

            middle_index = (upper_index + lower_index) // 2
            print(middle_index)
            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] < target:
                if middle_index == lower_index:
                    return middle_index + 1
                return find_index(nums, middle_index, upper_index, target)
            else:
                if middle_index == lower_index:
                    return max(0, middle_index - 1)
                return find_index(nums, lower_index, middle_index, target)
        
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            return find_index(nums, 0, len(nums)-1, target)