from unittest import TestCase, main

def solution(arr,k):
    result = float('inf')
    arr.sort()
    print(arr)     
    max_arr = [arr[i+k-1] - arr[i]  for i in range(0,len(arr)-k,k)]
    print(max_arr)
        
    return min(max_arr)

class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([1,4,7,2],2),1)
        self.assertEqual(solution([10,100,300,200,1000,20,30],3),20)
        self.assertEqual(solution([30,100,1000,150,60,250,10,120,20],3),20) #from max(30,10,20)-min(30,10,20),20, minimum unfairness in this sample
        self.assertEqual(solution([30,100,1000,150,60,250,10,120,20],5),90) #from max(30,100,60,10,20)-min(30,100,60,10,20),90, minimum unfairness in this sample
        self.assertEqual(solution([30,100,1000,150,34,1001,1002,1003,250,10,120,20],3),90) #from max(30,100,60,10,20)-min(30,100,60,10,20),90, minimum unfairness in this sample
        self.assertEqual(solution([1,1,1,1,1,1,1,1,1,2,2,2,2,2,2],10),1) #from max(1,1,1,1,1,1,1,1,1,2)-min(1,1,1,1,1,1,1,1,1,2),1, minimum unfairness in this sample
        self.assertEqual(solution([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],10),0) #from max(1,1,1,1,1,1,1,1,1,1)-min(1,1,1,1,1,1,1,1,1,1),0, minimum unfairness in this sample
        # self.assertEqual(solution([1,1,-1],2),0) #from max(1,1)-min(1,1),0, minimum unfairness in this sample
        self.assertEqual(solution([10,100,300,310,302,303],3),20)
        # self.assertEqual(solution(2,[1,4,7,2]),3)
        
        
if __name__ == "__main__":
    main()