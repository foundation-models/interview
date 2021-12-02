from unittest import TestCase, main
def solution(s, k):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if (s[i] + s[j]) % k != 0:
                count += 1

    return count
from collections import defaultdict

def solution2(s, k):
    mods = [item % k for item in s]
    freqs = defaultdict(int)
    for elem in mods:
        freqs[elem] += 1
    total = 0
    for key, val in freqs.items():
        if val == 0:
            continue
        if key == 0:
            total += 1
        elif (k - key) == key:
            total += 1
        elif key > (k - key):
            if (k - key) in freqs:
                total +=  max([val, freqs[k - key]])
            else:
                total += val
        elif key < (k - key):
            if (k - key not in freqs):
                total += val
    return total

class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution([1, 7, 2, 4], 3), 3)
        self.assertEqual(solution([278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436], 7), 11)
        
if __name__ == "__main__":
    main()
    
    