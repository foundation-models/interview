from unittest import TestCase, main

def jump_game_wrong(list, count = 0):
    if list is None or len(list) <= 1:
        return 0
    
    count += 1
    if list[0] >= len(list)-1:
        return count
    counts = []
    for i in range(1,min(len(list),list[0]+1)):
        new_count = jump_game(list[i:], count)
        if new_count is not None:
            if new_count - count == 1:
                return new_count
            counts.append(new_count)
    return min(counts) if len(counts) > 0 else None
    
def jump_game(list):
    N = len(list)
    if list is None or len(list) <= 1:
        return 0    
    
    farthest = list[0]
    count = 1
    
    start = 1
    for i in range(0, N):
        end = farthest
        for j in range(start, end+1):
            farthest = max(farthest, list[j] + j)
            print(farthest)
            if farthest >= N:
                count += 1
                return count
        start = end
        count += 1
    return count
    

    # for i in range(0,len(list)-1):
    #     for j in range(i+1, list[i] + i + 1):
    #         if j >= len(list):
    #             return count
    #         if list[j] + j + 1 > len(list):
    #             count += 1
    #             return count 
    # return count
        
    




class TestSolution(TestCase):
    
    def test_jump_game(self):
        self.assertEqual(jump_game([]), 0)
        self.assertEqual(jump_game([2]), 0)
        self.assertEqual(jump_game([2, 3]), 1)
        self.assertEqual(jump_game([2,3,1,1,4]), 2)
        self.assertEqual(jump_game([2,3,1,1,4,1]), 3)
        self.assertEqual(jump_game([2,0,2,4,6,0,0,3]), 3)
        


if __name__ == "__main__":
    main()

