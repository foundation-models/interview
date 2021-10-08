from typing import DefaultDict
from unittest import TestCase, main

def trim(list):
    result = ""
    index = 0
    while index < len(list):
        if list[index] is None:
            list.remove(list[index])
        else:
            index += 1
    print(list)
    return result.join(list)
    
        
def xxx(start, result, s, numRows):
    n = len(s)
    last_filled_index = 0
    for i in range(numRows):
        if start == len(s):
            return None
        last_filled_index = start + i * n
        result[last_filled_index] = s[start]
        start += 1
    for i in range(numRows-2):
        if start == len(s):
            return None
        j = i + 1
        result[last_filled_index- n*j+j] = s[start]
        start += 1
    return start
    
def zig_zag(s, numRows):

    result = [None] * numRows * len(s)
    start = 0
    while start is not None:
        start = xxx(start, result, s, numRows)
    return trim(result) 


class TestSolution(TestCase):
    
    def test_find_word_in_matrix(self):
        self.assertEqual(zig_zag( s = "PAYPALISHIRING", numRows = 3), "PAHNAPLSIIGYIR")
        self.assertEqual(zig_zag( s = "PAYPALISHIRING", numRows = 4), "PINALSIGYAHRPI")
        self.assertEqual(zig_zag( s = "A", numRows = 1), "A")


if __name__ == "__main__":
    main()