import unittest
from bst import *


# add more classes and tests

class EmptyTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.empty_tree = BSTree()

    #    def test_traverse(self):
    #      self.assertEqual(self.empty_tree.traverse(), [], "empty tree traversal is not empty")

    def test_height(self):
        self.assertEqual(self.empty_tree.height(), 0, "empty tree height is not 0")


class TreeTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = BSTree(BTNode(4, BTNode(3), BTNode(6, BTNode(5), BTNode(9))))

    def test_height(self):
        self.assertEqual(self.tree.height(), 3, "incorrect height")

    def test_contains(self):
        self.assertFalse(2 in self.tree)
        self.assertTrue(3 in self.tree)
        self.assertTrue(5 in self.tree)


class SoloInsertionTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = BSTree()
        self.tree.insert(-4)

    def test_contains(self):
        self.assertTrue(-4 in self.tree)
        self.assertFalse(3 in self.tree)

    def test_height(self):
        self.assertEqual(self.tree.height(), 1)


class MultiInsertionTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = BSTree()
        for a in [5, 3, 1, 4, 6, 4, 7, 88]:
            self.tree.insert(a)

    def test_insert(self):
        self.assertEqual(self.tree.root.value, 5)
        self.assertEqual(type(self.tree.root), BTNode)
        self.assertEqual(self.tree.root.left.value, 3)
        self.assertEqual(type(self.tree.root.left), BTNode)

    def test_contains(self):
        self.assertTrue(5 in self.tree)
        self.assertTrue(4 in self.tree)
        self.assertTrue(88 in self.tree)
        self.assertFalse(2 in self.tree)

    def test_height(self):
        self.assertEqual(self.tree.height(), 4)

    def test_is_bst(self):
        q = self.tree.traverse()
        self.assertEqual(q, sorted(q), "BST nodes violating  property")


if __name__ == "__main__":
    unittest.main()
