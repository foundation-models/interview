

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2**31 <= x <= (2**31 - 1):
            x_str = str(x)
            # print(x_str)
            first = x_str[0]
            result = "-" if first == '-' else ""
            for i in range(len(x_str),len(result),-1):
                result += x_str[i-1]
            result = int(result)
            if -2**31 <= result <= (2**31 - 1):
                return result 
            else:
                raise ValueError("Not a 32-bit integer")
        else:
            raise ValueError("Not a 32-bit integer")

from unittest import TestCase, main
class TestPractice(TestCase):
    
    def test_reverse(self):
        ob1 = Solution()
        self.assertEqual(ob1.reverse(-12030000), -3021)
        self.assertEqual(ob1.reverse(-120300001), -100003021)
        with self.assertRaises(ValueError):
            ob1.reverse(-1203000001000)
            ob1.reverse(-1203000005)

              
if __name__ == "__main__":
    main()