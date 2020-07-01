class UnionFind(object):
    def __init__(self, n):
        self.totalSize = self.components = n
        self.parent = [i for i in range(n)]
        self.size  = [1 for _ in range(n)]

    def find(self, p):

        root = p

        while (self.parent[root] != root):
            root = self.parent[root]

        while (self.parent[p] != p):
            temp = self.parent[p]
            self.parent[p] = root
            p = temp

        return root


    def union(self, p, q):

        rootp = self.find(p)
        rootq = self.find(q)

        if rootp == rootq:
            return

        if (self.size[rootp] > self.size[rootq]):
            self.size[rootp] += self.size[rootq]
            self.parent[rootq] = rootp

        else:
            self.size[rootq] += self.size[rootp]
            self.parent[rootp] = rootq
        # print(self.components)
        self.components -= 1


    def getNumberOfComponents(self):
        return self.components

    def getSize(self):
        return self.size

    def sameGroup(self, p, q):
        return self.find(p) == self.find(q)

if __name__ == '__main__':
    n = 10
    obj = UnionFind(n)
    # print(obj.components)  # 5
    obj.union(3, 2)
    obj.union(5, 9)
    obj.union(7, 5)
    obj.union(1, 2)
    obj.union(8, 5)
    obj.union(1, 5)
    obj.union(6, 5)


    print(obj.totalSize) #10
    print(obj.components) #3
    print(obj.sameGroup(1, 3)) # True
    # print(self.size)\
    print([i for i in range(n)]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(obj.parent) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(obj.size) #[1, 1, 3, 1, 1, 1, 1, 1, 1, 8]




