from unittest import TestCase, main



def bfs(board, x, y, visited):
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dx in delta:
        for dy in delta:
            new_x = x + dx
            new_y = y + dy
            x
    


def solve(board):
    
    
    # if we sint O, it should not be at first and end of that row
    
    # we iterate over each row and pick candidate and then iterate over each column and if we find and common candidates turn them into X
    row_candidate = []
    # iterate over board items and check if it is stitting in the border, we dont touch them

    i = 1
    j = 0
    while i < len(board)-1:
        while j < len(board[i]):
            # find first O in thr row
            o_index = board[i][j:].index("O")
            x_index = board[i][o_index:].index("X")
            if x_index == -1:
                continue
            if o_index == 0:
                j = x_index
            else:
                for k in range(o_index,x_index):
                    row_candidate.append((i,k))
    
        
    return board
    

class TestSolution(TestCase):
    
    def test_solve_board(self):
        self.assertEqual(solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]), [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])
        self.assertEqual(solve( [["X"]]),[["X"]])
    
if __name__ == "__main__":
    main()