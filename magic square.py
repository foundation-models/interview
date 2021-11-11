from unittest import TestCase, main

def solution(s):
    sums = []
    for i,row in enumerate(s):
        sums.append(sum(row))
        sums.append(sum(row[i][j]))
    print(sums)
        
    return sums

class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([[5, 3, 4], [1, 5, 8], [6, 4, 2]]),7)

        
        
if __name__ == "__main__":
    main()