from unittest import TestCase, main

def solution0(expenditure, d):
    if d >= len(expenditure):
        return 0
    alers = 0
    for i in range(len(expenditure) - d):
        average = sum(expenditure[i:i+d])/d
        if expenditure[i+d] >= 2*average:
            alers += 1
    return alers
        
def solution1(expenditure, d):
    if d >= len(expenditure):
        return 0
    alers = 0
    average = sum(expenditure[0:d])/d
    for i in range(len(expenditure) - d):
        if i > 0:
            average += (expenditure[i+d-1] - expenditure[i-1]) / d
        if expenditure[i+d] >= 2*average:
            alers += 1
    return alers


def solution(expenditure, d):
    alerts = 0
    for i in range(d, len(expenditure)):
        days = expenditure[i-d:i]
        arr = sorted(days)
        if d%2 != 0:
            median = arr[(d+1)//2 - 1]
        else:
            median = (arr[(d)//2 - 1] + arr[(d+1)//2])/2
        if expenditure[i] >= 2*median:
            alerts +=1
    return alerts

class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([10,20,30,40,50],3),1)
        self.assertEqual(solution([2, 3, 4, 2, 3, 6, 8, 4, 5],5),2)

        
        
if __name__ == "__main__":
    main()