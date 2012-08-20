import unionfind
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.arr = unionfind.UnionFind(10)

    def test_init(self):
        self.assertEqual(self.arr.idArray, range(10))

    def test_union(self):
        self.arr.union(2,3)
        self.assertEqual(self.arr.connected(2,3),True)

        self.arr.union(3,5)
        self.assertEqual(self.arr.connected(3,5),True)
        
    def test_connected(self):
        self.arr.union(3,5)
        self.assertEqual(self.arr.connected(3,5),True)
        self.assertEqual(self.arr.connected(1,2),False)

    def test_root(self):
        self.arr.union(2,3)        

        self.assertEqual(self.arr.root(2),3)
        self.assertEqual(self.arr.root(3),3)
        
        self.arr.union(3,5)

        self.assertEqual(self.arr.root(2),5)
        self.assertEqual(self.arr.root(3),5)

    def test_quick_union(self):
        self.arr.quick_union(2,3)
        self.assertEqual(self.arr.quick_connected(2,3),True)
        
        self.arr.quick_union(3,5)
        self.assertEqual(self.arr.quick_connected(3,5),True)

    def test_quick_connected(self):
        self.arr.union(3,5)
        self.assertEqual(self.arr.quick_connected(3,5),True)
        self.assertEqual(self.arr.quick_connected(1,2),False)

if __name__ == '__main__':
    unittest.main()
