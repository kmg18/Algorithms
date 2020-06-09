class BSTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def search(self, data):

        root = self.root
        while root:

            if root.val == data:
                return True

            if root.val > data:
                root = root.left
            elif root.val < data:
                root = root.right

        return False


    def insert(self, data):
        node = BSTNode(data)
        if self.root is None:
            self.root = node
            return data

        root = self.root

        while root:
            if node.val <= root.val:
                if not root.left:
                    root.left = node
                    break
                root = root.left
            else:
                if not root.right:
                    root.right = node
                    break
                root = root.right
        return data




if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10) #10
    bst.insert(20) #20
    bst.insert(50) #30

    bst.search(20) #True
    bst.search(30) #False



