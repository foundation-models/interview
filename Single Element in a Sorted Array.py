from unittest import TestCase, main


def binary_search(arr, to_find, i, j):
    if arr[i] == to_find:
        return i
    if i + 1 == j or i == j:
        return -1
    mid = (i + j) // 2
    if arr[mid] <= to_find:
        return binary_search(arr, to_find, mid, j)
    else:
        return binary_search(arr, to_find, i, mid)

# right answer   
def search(arr, n):
 
    ans = -1
    for i in range(0, n, 2):
        if (arr[i] != arr[i + 1]):
            ans = arr[i]
            break
    if(arr[n-2] != arr[n-1]):
        ans = arr[n-1]
 
    # ans = -1 if no such element is present.

def solution(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    
    
    nums.sort()
    
    def find(i, j, get_lower=True):
        if i + 1 == j:
            return nums[i] if get_lower else nums[j]
        mid = (i + j) // 2
        if nums[mid - 1] != nums[mid]:
            if nums[mid] != nums[mid + 1]:
                return nums[mid]
            else:
                return find(mid, j, False) if (j - i) // 2 % 2 == 0 else find(i, mid, True)
        elif nums[mid] != nums[mid + 1]:
            return find(i, mid, True)  if (j - i) // 2 % 2 == 0 else find(mid, j, False)
        else:
            raise NotImplemented()  
        
    return find(0, len(nums)-1)
        
    



class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([]),None)
        self.assertEqual(solution([2]),2)
        self.assertEqual(solution([2,2,3]),3)
        self.assertEqual(solution([2,2,1]),1)
        self.assertEqual(solution([2,2,3,4,4]),3)
        self.assertEqual(solution([2,2,3,3,4]),4)
        self.assertEqual(solution([2,2,3,3,1]),1)
        self.assertEqual(solution([2,2,1]),1)
        self.assertEqual(solution([1,1,2,3,3,4,4,8,8]),2)


if __name__ == "__main__":
    main()