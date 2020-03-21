# -*- coding: utf-8 -*-
from tree import Tree


class AVLTree(Tree):
    """An abstraction of Balanced AVL Tree"""

    def __init__(self, key=None, parent=None):
        super(AVLTree, self).__init__(key, parent)
        self.height = 0

    def __repr__(self):
        return (
            'AVLTree(key={}, '
            'parent={}, '
            'left={}, '
            'right={}, '
            'height={})'
        ).format(
            self.key,
            self.parent.key if self.parent else None,
            self.left.key if self.left else None,
            self.right.key if self.right else None,
            self.calculate_height(),
        )

    def calculate_height(self):
        """
        Calculate the height of a tree getting the max height of a tree plus 1.

        :return: tree height
        """
        if self.is_leaf():
            return 0

        left_height = self.left.calculate_height() if self.left else 0
        right_height = self.right.calculate_height() if self.right else 0

        self.height = max(left_height, right_height) + 1
        return self.height

    def left_rotate(self):
        """
        Implements a left rotation in the tree.

        :return: new root of the tree
        """
        temp = self.right

        self.right = temp.left
        if self.right:
            self.right.parent = self

        temp.left = self
        temp.parent = self.parent
        self.parent = temp

        return temp

    def right_rotate(self):
        """
        Implements a right rotation in the tree.

        :return: new root of the tree
        """
        temp = self.left

        self.left = temp.right
        if self.left:
            self.left.parent = self

        temp.right = self
        temp.parent = self.parent
        self.parent = temp

        return temp

    def left_right_rotate(self):
        """
        Implements a left-right rotation in the tree using the left and right
        basic rotations.

        :return: new root of the tree
        """
        self.left = self.left.left_rotate()
        return self.right_rotate()

    def right_left_rotate(self):
        """
        Implements a right-left rotation in the tree using the left and right
        basic rotations.

        :return: new root of the tree
        """
        self.right = self.right.right_rotate()
        return self.left_rotate()

    def rebalance(self):
        """
        Rebalance uses the 4 basic rotations to balance a tree and preserve the
        AVL Tree balance properties.
        Example:
            8
           /        6
          6    =>  / \
         /        4   8
        4

        :return: The method always return the new balanced root of the tree
        """
        l_height = self.left.calculate_height() + 1 if self.left else 0
        r_height = self.right.calculate_height() + 1 if self.right else 0

        if abs(l_height - r_height) > 1:
            if l_height > r_height:
                temp = self.left

                pl_height = (
                    temp.left.calculate_height() + 1
                ) if temp.left else 0

                pr_height = (
                    temp.right.calculate_height() + 1
                ) if temp.right else 0

                if pl_height > pr_height:
                    return self.right_rotate()
                else:
                    return self.left_right_rotate()
            else:
                temp = self.right

                pl_height = (
                    temp.left.calculate_height() + 1
                ) if temp.left else 0

                pr_height = (
                    temp.right.calculate_height() + 1
                ) if temp.right else 0

                if pl_height > pr_height:
                    return self.right_left_rotate()
                else:
                    return self.left_rotate()

        return self

    def insert(self, key):
        """
        Implements AVLTree insertion recursively. The insertion preserves the
        AVL Tree property, which means it can change the root to keep the tree
        balanced.

        Example:
            root = root.insert(89)

        This method always returns the root of the tree, which means that to
        keep always the root reference it's required to use the returned value
        of the insertion.

        Specialy to smaller trees, the insertion can cause an unbalanced tree,
        so after every the insertion the return always rebalance the tree.

        :param key: Key to be inserted in the tree
        :return self: New tree root
        """

        if not self.key:
            self.key = key
            return self

        if self.key > key:
            if not self.left:
                self.left = AVLTree(key, self)
                return self
            else:
                self.left.insert(key)
                return self.rebalance()

        if self.key < key:
            if not self.right:
                self.right = AVLTree(key, self)
                return self
            else:
                self.right.insert(key)
                return self.rebalance()

        raise DuplicatedKeyError(
            'DuplicatedKeyError: {} is already in the tree'.format(key)
        )
