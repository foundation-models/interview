from unittest import TestCase, main
from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  reserved = [False] * N
  for s in S:
    for i in range(max(s-1-K,0),min(s+K,N)):
      reserved[i] = True   
  count = 0
  x = 0
  while(x < N):
    try:
        x += reserved[x:].index(False)
    except ValueError:
        break
    if 0<=x<N-1:
      y = x + 1
      while(y < N):
        try:
            y += reserved[y:].index(False)
        except ValueError:
            x = N
            break
        if y - x >= K:
          count += 1
          x = y
          break
        else:
          y += 1
    elif x == N - 1:
      count += 1
      x += 1
  return count

class TestSolution(TestCase):
    
    def test_solve_board(self):
        self.assertEqual(getMaxAdditionalDinersCount(N = 10, K = 1, M = 2, S = [2, 6]), 3)
        self.assertEqual(getMaxAdditionalDinersCount(N = 15, K = 2, M = 3, S = [11, 6, 14]), 1)    
if __name__ == "__main__":
    main()
    