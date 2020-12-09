class BTNode:
    ''' This class is complete. '''

    def __init__(self, val, l=None, r=None):
        '''Create new BTNode with value val
        and optional left child l and right child r.
        This method is complete.'''

        self.value = val
        self.left = l
        self.right = r

    def __str__(self):
        '''Return the string representation of this BTNode's value.
        This method is complete.'''

        return str(self.value)


class BSTree:

    def __init__(self, root=None):
        '''Create a new BST with optional root root.
        This method is complete.'''

        self.root = root

    def __str__(self):
        '''Return a string representing a left-tilted representation of the tree.
        This method is complete.
        '''

        return self._print(self.root, 0)

    def _print(self, node, depth):
        '''Return a string representing a left-tilted version of subtree
        rooted at node given node's depth.
        This method is complete.'''

        if not node:
            return ""

        right_tree = self._print(node.right, depth + 1)
        left_tree = self._print(node.left, depth + 1)
        node_str = "\t" * depth + str(node) + '\n'
        return right_tree + node_str + left_tree

    def traverse(self):
        '''Return a list of all values in the tree from left to right.
        This method is complete.'''

        return self._traverse(self.root)

    def _traverse(self, node):
        '''Return a list of all values in the tree rooted at node from
        left to right. This method is complete.'''

        if not node:
            return []
        l = []
        l.extend(self._traverse(node.left))
        l.append(node.value)
        l.extend(self._traverse(node.right))
        return l

    ### Part 1: Insertion ###

    def insert(self, value):
        """Insert value into self.
        This method is complete."""

        if not self.root:
            self.root = BTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """Insert value into BST rooted at node."""
        if value < node.value:
            if node.left is None:
                node.left = BTNode(value)
            else:
                self._insert(node.left, value)
        if value > node.value:
            if node.right is None:
                node.right = BTNode(value)
            else:
                self._insert(node.right, value)
    ### Part 2: Membership ###

    def __contains__(self, v):
        """Return True iff BST self contains value v.
        This method is complete."""

        return self._contains(self.root, v)

    def _contains(self, node, v):
        """Return True iff BST rooted at node contains value v."""
        # print(node)
        if node is None:
            return False

        if node.value == v:
            return True
        if v < node.value:
            return self._contains(node.left, v)
        else:
            return self._contains(node.right, v)

    def height(self):
        """Return the length of the longest path from the root of self
        to a leaf. This method is complete."""

        return self._height(self.root)

    def _height(self, node):
        """Return the height of tree rooted at node."""
        left_height, right_height = 0, 0
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


if __name__ == "__main__":
    t1 = BSTree(BTNode(4, BTNode(3), BTNode(6, BTNode(5), BTNode(9))))
    print(t1)
    print(t1.traverse())
    print(t1.height())
    print(5 in t1)

    t2 = BSTree()
    for a in [6, 7, 2, 3, 1, 4, 7, 99, 0]:
        # print('value: ')
        # print(a)
        t2.insert(a)
        # print('t2')
        # print(t2)
    print('t2: ')
    print(t2)
