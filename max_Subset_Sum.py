from unittest import TestCase, main

def maxSubsetSum(arr):
    
    # check out https://youtu.be/n9F9wQD3Mhc

    def make_subset(arr, result, j):
        if len(arr) < 1:
            return result
        i = 0
        while(i+j < len(arr)):

            i += 1
        print(i, j, result, sum(arr), arr)
        result = max(result, sum(arr))
        if len(arr) > 1:
            result = make_subset(arr, result, j)
        return result
    result = 0
    i = 0
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            result = make_subset(arr[i:], result, j)
    print(result)
    # print(make_subset(arr[i:]))

    # print(make_subset(i, arr))
    # print(make_subset(i, arr))
    # print(make_subset(i, arr))
    return result
    




class TestSolution(TestCase):
    
    def test_maxSubsetSum(self):
        self.assertEqual(maxSubsetSum([3, 7, 4, 6, 5]), 13)
        self.assertEqual(maxSubsetSum([3, 5, -7, 8, 10]), 15)
        self.assertEqual(maxSubsetSum([2, 1, 5, 8, 4]), 11)


        


if __name__ == "__main__":
    main()

