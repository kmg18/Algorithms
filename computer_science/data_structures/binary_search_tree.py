class BSTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def findMin(self, root):
        while root.left:
            root = root.left
        return root

    def search(self, data):

        root = self.root
        while root:

            if root.val == data:
                return True

            if data < root.val:
                root = root.left
            elif data > root.val:
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

    def deleteNode(self, root, key):

        if root is None:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None

            elif not root.right:
                root = root.left
            elif not root.left:
                root = root.right

            else:
                minVal = self.findMin(root.right)
                root.val = minVal.val
                root.right = self.deleteNode(root.right, minVal.val)
        return root

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10) #10
    bst.insert(20) #20
    bst.insert(50) #30

    bst.search(20) #True
    bst.search(30) #False



