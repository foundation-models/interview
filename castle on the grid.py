from unittest import TestCase, main
from collections import defaultdict
from collections import Counter

# https://youtu.be/OM5hC6rOIM8
        
def minimumMoves(grid, startX, startY, goalX, goalY):
    
    queue = [(startX, startY, 0)]
    visited = set((startX, startY))
    moves = [[1,0], [-1,0], [0,1], [0,-1]] # [[1,0], [0,1], [0,-1], [-1,0]]
    while(len(queue) > 0):
        x_init, y_init, count = queue.pop(0)
        count += 1
        for x_move, y_move in moves:
            x, y = x_init, y_init
            while(True):
                x += x_move
                y += y_move

                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X':
                    if x == goalX and y == goalY:
                        return count
                    elif (x, y) not in visited:
                        visited.add((x, y))
                        queue.append((x,y,count))
                else:
                    break
    return -1
            



class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(minimumMoves(['.X.','.X.', '...'],0, 0, 0, 2),3)


        
if __name__ == "__main__":
    main()