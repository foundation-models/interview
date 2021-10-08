from typing import DefaultDict
from unittest import TestCase, main

from is_BST import list_to_BST


def next_possible_indices_2d(i, N, j, M):
    result = []
    result_i = next_possible_indices_1d(i, N)
    result_j = next_possible_indices_1d(j, M)
    for x in result_i:
        for y in result_j:
            result.append((x,y))
    result.remove((i,j))
    return result

def next_possible_indices(indices, allowed_list):
    result = []
    for index in indices:
        if index in allowed_list:
            result.append(index)
    return result

def next_possible_indices_1d(i, N):
    result = [i] 
    if i-1 > -1:
        result.append(i-1)
    if i+1 < N:
        result.append(i+1)
    return result

def find_word_in_matrix(board, word):
    if board is None or len(board) == 0:
        return False
    if word is None or len(word) == 0:
        return True
    # assume matrix is diagonal
    
    N = len(board)
    M = len(board[0])
    visited = [[False] * M]  * N
    
    map = DefaultDict(list)
    
    for i, line in enumerate(board):
        for j, char in enumerate(line):
            map[char].append((i,j))
    
    candidates = []
    for char in word:
        if char not in map: 
            return False


        
    def xx(candidate, possible_indices):
        result = []
        for i, j in candidate: 
            result.extend(next_possible_indices(next_possible_indices_2d(i, N, j, M), possible_indices))
        return result    

    result = map[word[0]]
    for i in range(1, len(word)):
        result = xx(result, map[word[i]])
        if len(result) == 0:
            return False

    return True


class TestSolution(TestCase):
    
    def test_find_word_in_matrix(self):
        self.assertFalse(find_word_in_matrix([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
        self.assertTrue(find_word_in_matrix( [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
        self.assertTrue(find_word_in_matrix([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))




if __name__ == "__main__":
    main()