from unittest import main, TestCase

# Returns index of x in arr if present, else -1
def Binary_Search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

def binary_search(s):
    def b_search(i, j):
        if i > j:
            return NotImplementedError
        elif i == j:
            return None
        if i + 1 == j:
            return i # i inclusive
        
        k = (i + j) // 2
        if s[i] < s[k]:
            return b_search(k, j)
        else:
            return b_search(i, k)

    k = b_search(0, len(s))
    if k is None:
        return []
    result = s[k+1:len(s)]
    result.extend(s[0:k+1])
    return result

class TestX(TestCase):
    def test_x(self):
        self.assertEqual(binary_search([]), [])
        self.assertEqual(binary_search([3,4,1,2]), [1,2,3,4])
        self.assertEqual(binary_search([3,4,5,6,1,2]), [1,2,3,4,5,6])

if __name__ == "__main__":
    main()