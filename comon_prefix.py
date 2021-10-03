from typing import DefaultDict, Iterable
from itertools import permutations

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Python program to convert a list
        # of character
        
        def convert(s):
            new = ""
            for x in s:
                new += x 
            return new
      
        
        result = ""
        # create two dictionaries:
        # 1. maps every character to the list of indices of strings in the strs that contains that chanacter
 
        def find_in_this_list(this_list):
            container_indices = DefaultDict(list)
            for char in this_list:
                for index, str in enumerate(strs):
                    if char in str:
                        container_indices[char].append(index)
            print(container_indices)
            return [char for char in container_indices.keys() if len(container_indices[char]) == len(strs)]

        def find_in_permutation(candidates):
            for element in permutations(candidates):
                this_list.append(convert(element))
            new_candidate = find_in_this_list(this_list)
            if len(new_candidate) == 0:
                return candidates
            elif len(new_candidate) == 1:
                return new_candidate
            else:
                return find_in_permutation(new_candidate)
            
        import string
        this_list = list(string.ascii_lowercase)
        candidates = find_in_this_list(this_list)
        this_list = []
        return find_in_permutation(candidates)

            
                

        # 2. maps tuple of (character, index) to list of indices of that character that strs[index]
        
        
        
        # then if lenght of values is 
        expected_index = 0
        for str in strs:
            for candidate in str:
                for str in strs:
                    if find(str, candidate, expected_index):
                        pass
                    else:
                        return result
                result += candidate
        print(result)
        return result
    
from unittest import TestCase, main
class TestPractice(TestCase):
    
    def test_solution(self):
        ob1 = Solution()
        # self.assertEqual(ob1.longestCommonPrefix(["flower","flow","flight"]), ["fl"])
        
        # self.assertEqual(ob1.longestCommonPrefix(["flower",]), ["flower"])
        
        self.assertEqual(ob1.longestCommonPrefix(["flower","xloxer"]), ["lo", "er"])



        # with self.assertRaises(ValueError):
        #     ob1.longestCommonPrefix(-1203000001000)


              
if __name__ == "__main__":
    main()