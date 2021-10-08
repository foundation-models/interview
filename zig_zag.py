from typing import DefaultDict
from unittest import TestCase, main

def trim(list):
    result = ""
    for i in range(len(list)):
        result += ''.join(list[i])
    return result

    
        
def xxx(start, result, s, numRows):
    n = len(s)
    for i in range(numRows):
        if start >= n:
            return None
        if i == len(result):
            result.append([])
        result[i].append(s[start])
        start += 1
    for i in range(numRows-2,0,-1):
        if start >= n:
            return None
        # result[i].extend([None]*i)
        result[i].append(s[start])
        start += 1
    return start
    
def zig_zag(s, numRows):

    result = []
    start = 0
    while start is not None:
        start = xxx(start, result, s, numRows)
    return trim(result) 


class TestSolution(TestCase):
    
    def test_find_word_in_matrix(self):
        self.assertEqual(zig_zag( s = "PAYPALISHIRING", numRows = 3), "PAHNAPLSIIGYIR")
        self.assertEqual(zig_zag( s = "PAYPALISHIRING", numRows = 4), "PINALSIGYAHRPI")
        self.assertEqual(zig_zag( s = "A", numRows = 1), "A")
        self.assertEqual(zig_zag( s = "nwwzcdsxrhcolbbdddhmvuhvgaymcpyrlxq", numRows = 15), " ncwmpwyyzarcgldvxshqxurvhmchodldbdb")


if __name__ == "__main__":
    main()