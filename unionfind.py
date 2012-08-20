class UnionFind:

    def __init__ (self,n):
        self.idArray = range(n)

    def union(self,p,q):
        pid = self.idArray[p]
        qid = self.idArray[q]

        self.idArray = [qid if i == pid else i for i in self.idArray]

    def quick_union(self,p,q):
        i = self.root(p)
        j = self.root(q)
        self.idArray[i] = j

    def connected(self,p,q):
        return self.idArray[p] == self.idArray[q]

    def root(self,p):
        while (self.idArray[p] != p):
            p = self.idArray[p]
        return p

    def quick_connected(self,p,q):
        return self.root(p) == self.root(q)
