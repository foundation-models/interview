from unittest import main, TestCase

def binary_search(s):
    def b_search(i, j):
        if i > j:
            return NotImplementedError
        elif i == j:
            return None
        if i + 1 == j:
            return i # i inclusive
        
        k = (i + j) // 2
        if s[i] < s[k]:
            return b_search(k, j)
        else:
            return b_search(i, k)

    k = b_search(0, len(s))
    if k is None:
        return []
    result = s[k+1:len(s)]
    result.extend(s[0:k+1])
    return result

class TestX(TestCase):
    def test_x(self):
        self.assertEqual(binary_search([]), [])
        self.assertEqual(binary_search([3,4,1,2]), [1,2,3,4])
        self.assertEqual(binary_search([3,4,5,6,1,2]), [1,2,3,4,5,6])

if __name__ == "__main__":
    main()