import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

    def __str__(self):
        return str(self.info) 
    
    
    def __repr__(self):
        return str(self.info) 
    
def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()

    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


def decodeHuff(root, s):
    
    # Base Case
    if root is None:
        return None
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
    return root    
    

def solution(arr, v1, v2):
    root = huffman_hidden()#contains root of huffman tree

    code_hidden = {}#contains code for each object

    dfs_hidden(root, "")

    if len(code_hidden) == 1:#if there is only one character in the i/p
        for key in code_hidden:
            code_hidden[key] = "0"

    toBeDecoded = ""

    for ch in ip:
        toBeDecoded += code_hidden[ch]
    return decodeHuff(root, toBeDecoded)


class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([4,2,3,1,7,6], 1, 7),4)
        self.assertEqual(solution([2,1,4,3,5,6], 3, 6),4)


if __name__ == "__main__":
    main()