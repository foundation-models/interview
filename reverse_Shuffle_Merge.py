from unittest import TestCase, main

def reverseShuffleMerge(st):
    candiate = st[:len(st)//2]
    print(candiate)
    




class TestSolution(TestCase):
    
    def test_jump_game(self):
        self.assertEqual(reverseShuffleMerge("aeiouuoiea"), "aeiou")

        


if __name__ == "__main__":
    main()

