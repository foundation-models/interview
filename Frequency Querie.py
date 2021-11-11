from unittest import TestCase, main
from collections import defaultdict
from collections import Counter

        
def solution(queries):
    freq = Counter()
    cnt = Counter()
    result = []
    for action, value in queries:
        if action == 1:
            cnt[ freq[value] ] -= 1
            freq[value] += 1
            cnt[ freq[value] ] += 1
        elif action == 2:
            if freq[value] > 0:
                cnt[ freq[value] ] -= 1
                freq[value] -= 1
                cnt[ freq[value] ] += 1
        else:
            result.append(1 if cnt[value] > 0 else 0)
    return result

def solution1(queries):
    results = []
    lookup = dict()
    freqs = defaultdict(set)
    for command, value in queries:
        freq = lookup.get(value, 0)
        if command == 1:
            lookup[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        elif command == 3:
            results.append(1 if freqs[value] else 0)
    return results  


class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([(1,1) ,(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]),[0,1])
        self.assertEqual(solution([(1,5), (1,6),(3,2),(1,1),(1,1),(2,1),(3,2)]),[0,0])





        
        
if __name__ == "__main__":
    main()