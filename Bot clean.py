from unittest import TestCase, main



def next_move(r, c, board): 
    if board[r][c] == 'd':
        print('CLEAN')
        return None    
    n = len(board)           
    dirties = [ ((i - r)**2 + (j - c)**2, i, j) for i in range(n) for j in range(n) if board[i][j] == 'd']
    dirties.sort()
    _, i, j = dirties[0]
    if i > r:
        print("DOWN")
    elif i < r:
        print("UP")
    elif j > c:
        print("RIGHT")
    elif j < c:
        print("LEFT")
    return None
                       
def solution(r, c, board):
    return next_move(r, c, board)


class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution(2, 1, ['d--','---','d--']),'LEFT')




        
        
if __name__ == "__main__":
    main()