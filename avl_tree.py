# -*- coding: utf-8 -*-
class TreeNode(object):
    """
    Simple implementation of a Tree Node
    """
    def __init__(self, key):
        super(TreeNode, self).__init__()
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return (
            'Node(key={}, '
            'left={}, '
            'right={}, '
            'height={})'
        ).format(
            self.key,
            self.left.key if self.left else None,
            self.right.key if self.right else None,
            self.height,
        )


class AVLTree(object):
    """
    An abstraction of Balanced AVL Tree. This class is thought as a blueprint to
    format the tree passed as root in its methods.

    The AVLTree object itself has no root or nodes within it, but its methods
    take a root to work with
    """
    class DuplicatedKeyError(Exception):
        pass

    def get_height(self, root):
        """
        Get the height of the root

        :return: integer with the height
        """
        if root is None:
            return 0

        return root.height

    def get_balance(self, root):
        if root is None:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    # --------------------------------------------------------------------------
    # AVL Tree Rotation --------------------------------------------------------
    # --------------------------------------------------------------------------
    def left_rotate(self, root):
        """
        Implements a left rotation in the tree.

        :return: new root
        """
        temp = root.right
        root.right = temp.left
        temp.left = root

        return temp

    def right_rotate(self, root):
        """
        Implements a right rotation in the tree.

        :return: new root of the tree
        """
        temp = root.left
        root.left = temp.right
        temp.right = root

        return temp

    def left_right_rotate(self, root):
        """
        Implements a left-right rotation in the tree using the left and right
        basic rotations.

        :return: new root of the tree
        """
        root.left = self.left_rotate(root.left)
        return self.right_rotate(root)

    def right_left_rotate(self, root):
        """
        Implements a right-left rotation in the tree using the left and right
        basic rotations.

        :return: new root of the tree
        """
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)

    # --------------------------------------------------------------------------
    # AVL Utility Methods ------------------------------------------------------
    # --------------------------------------------------------------------------
    def search(self, root, key):
        """
        Implements AVLTree search recursively.

        :param root: root tree to search
        :param key: value to be searched
        :return: tree if found or None otherwise
        """
        if root is None:
            return None
        elif root.key > key:
            return self.search(root.left, key)
        elif root.key < key:
            return self.search(root.right, key)
        else:
            return root

    def insert(self, root, key):
        """
        Implements AVLTree insertion recursively. The insertion preserves the
        AVL Tree property, which means it can change the root to keep the tree
        balanced.

        Example:
            root = tree.insert(root, 89)

        This method always returns the root of the tree, which means that to
        keep always the root reference it's required to use the returned value
        of the insertion.

        Specialy to smaller trees, the insertion can cause an unbalanced tree,
        so after every the insertion the return always rebalance the tree.

        :param root: tree to be inserted
        :param key: Key to be inserted in the tree
        :return self: New tree root
        """
        if root is None:
            return TreeNode(key)
        elif root.key > key:
            root.left = self.insert(root.left, key)
        elif root.key < key:
            root.right = self.insert(root.right, key)
        else:
            raise DuplicatedKeyError(
                'DuplicatedKeyError: {} is alrefy in the AVL Tree'.format(key)
            )

        root.height = max(
            self.get_height(root.left),
            self.get_height(root.right),
        ) + 1

        balance = self.get_balance(root)


        if balance > 1 and key < root.left.key:
            # left - left unbalance
            return self.right_rotate(root)
        elif balance > 1 and key > root.left.key:
            # left - right unbalance
            return self.left_right_rotate(root)
        elif balance < -1 and key > root.right.key:
            # right - right unbalance
            return self.left_rotate(root)
        elif balance < -1 and key < root.right.key:
            # right - left unbalance
            return self.right_left_rotate(root)

        return root

    def inorder(self, root):
        """
        Prints the inorder path in the tree.

        :param root: tree to be printed
        """
        if root is None:
            return

        self.inorder(root.left)
        print(' {} '.format(root.key), end='')
        self.inorder(root.right)
        return
