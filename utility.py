
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            
    def __str__(self) -> str:
        if self.left is None and self.right is None:
            return "{} val: {} {}".format('{', self.val or "-", '}') 
        return "{} val: {}, left: {}, right: {} {}".format('{', self.val, self.left or "-", self.right or "-", '}')   