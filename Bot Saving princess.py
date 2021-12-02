from unittest import TestCase, main



from collections import deque
def save_princess(N, matrix):

    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    moves_st = { (1,0): 'DOWN', (-1,0): 'UP', (0,1): 'RIGHT', (0,-1): 'LEFT'}
    actions = []
    visited = set()
    # this is probably wrong
    for i, j in zip(range(N),range(N)):
        if matrix[i][j] == 'm':
            break
    visited.add((i,j))
    q = [(i,j,actions)]
    while q:
        init_i, init_j, actions = q.pop(0)
        for d_i, d_j in moves:
            i = init_i + d_i
            j = init_j + d_j
            if 0 <= i < N and 0 <= j < N and (i,j) not in visited:
                if matrix[i][j] == 'p':
                    return actions + [moves_st[(d_i, d_j)]]
                visited.add((i,j))
                q.append((i,j,actions + [moves_st[(d_i, d_j)]]))
    return actions

                    
        
def solution(matrix):
    return save_princess(matrix)


class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(['---','-m-','p--']),['DOWN','LEFT'])




        
        
if __name__ == "__main__":
    main()