from unittest import TestCase, main

from is_BST import list_to_BST

def find_mode_in_BST(root):

    def inorder(root, prev, cnt, max_cnt, result):
        if not root:
            return prev, cnt, max_cnt

        prev, cnt, max_cnt = inorder(root.left, prev, cnt, max_cnt, result)
        if prev:
            if root.val == prev.val:
                cnt += 1
            else:
                cnt = 1
        if cnt > max_cnt:
            max_cnt = cnt
            del result[:]
            result.append(root.val)
        elif cnt == max_cnt:
            result.append(root.val)
        return inorder(root.right, root, cnt, max_cnt, result)

    result = []
    inorder(root, None, 1, 0, result)
    return result

class TestSolution(TestCase):
    
    def test_find_mode_in_BST(self):
        self.assertEqual(find_mode_in_BST(list_to_BST([])), [])
        self.assertEqual(find_mode_in_BST(list_to_BST([0])), [0])
        self.assertEqual(find_mode_in_BST(list_to_BST([2,1,2])), [2])
        self.assertEqual(find_mode_in_BST(list_to_BST([1,None,2,2])), [2])



if __name__ == "__main__":
    main()