from unittest import TestCase, main

convert = { 6:"six", 13: "thirteen", 5:"five" }

def solution(h, m):
    # Write your code here
    answer = ""
    if m > 30:      
        answer += convert[60-m] + " minutes to " + convert[h+1]
    elif m == 30:
        answer += "half past " + convert[h]
        
    return answer


    



class TestPractice(TestCase):
    def test_soluton(self):
        self.assertEqual(solution(5, 47), 'thirteen minutes to six')
        self.assertEqual(solution(5, 30), 'thalf past five')
        


              
if __name__ == "__main__":
    main()