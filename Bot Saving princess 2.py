from unittest import TestCase, main


def save_princess(n, r, c, board):
    abort = False
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'p':
                abort = True
                break
        if abort:
            break
    if i > r:
        return "DOWN"
    elif i < r:
        return "UP"
    elif j > c:
        return "RIGHT"
    elif j < c:
        return "LEFT"


class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(save_princess(3,0,0,['---','-m-','p--']),'DOWN')


        
        
if __name__ == "__main__":
    main()