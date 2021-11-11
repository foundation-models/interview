from unittest import TestCase, main

def solution(prices, k):
    prices.sort()
    sum = 0
    i = 0
    for price in prices:
        sum += price
        if sum >= k:
            break
        else:
            i += 1
    return i
        

class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([1, 12 ,5 ,111 ,200,1000 ,10], 50),4)

        
        
if __name__ == "__main__":
    main()