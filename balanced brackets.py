from unittest import TestCase, main
from collections import defaultdict
from collections import Counter

        
def solution(s):

    brackets = []
    for ch in s:
        if ch == '{':
            brackets.append(1)
        elif ch == '[':
            brackets.append(2)
        elif ch == '(':
            brackets.append(3)
        elif ch == '}' and brackets.pop() != 1:
            return 'NO'
        elif ch == ']' and brackets.pop() != 2:
                return 'NO'               
        elif ch == ')' and brackets.pop() != 3:
            return 'NO'
    if len(brackets) == 0:
        return 'YES'
    else:
        return 'NO'
    




class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution('{[()]}'),'YES')
        self.assertEqual(solution('{[(])}'),'NO')
        self.assertEqual(solution('{{[[(())]]}}'),'YES')


        
if __name__ == "__main__":
    main()