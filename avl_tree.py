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
        if self.is_leaf():
            return 0

        left_height = self.left.calculate_height() if self.left else 0
        right_height = self.right.calculate_height() if self.right else 0

        self.height = max(left_height, right_height) + 1
        return self.height

    def left_rotate(self):
        temp = self.right

        self.right = temp.left
        if self.right:
            self.right.parent = self

        temp.left = self
        temp.parent = self.parent
        self.parent = temp

        return temp

    def right_rotate(self):
        temp = self.left

        self.left = temp.right
        if self.left:
            self.left.parent = self

        temp.right = self
        temp.parent = self.parent
        self.parent = temp

        return temp

    def left_right_rotate(self):
        self.left = self.left.left_rotate()
        return self.right_rotate()

    def right_left_rotate(self):
        self.right = self.right.right_rotate()
        return self.left_rotate()

    def rebalance(self):
        l_height = self.left.calculate_height() + 1 if self.left else 0
        r_height = self.right.calculate_height() + 1 if self.right else 0

        if abs(l_height - r_height) > 1:
            print('unbalanced ' + str(self.key))

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
        """Implements AVLTree insertion recursively"""
        if not self.key:
            self.key = key
            return self

        if self.key > key:
            if not self.left:
                self.left = AVLTree(key, self)
                return self.left
            else:
                self.left.insert(key)
                return self.rebalance()

        if self.key < key:
            if not self.right:
                self.right = AVLTree(key, self)
                return self.right
            else:
                self.right.insert(key)
                return self.rebalance()

        raise DuplicatedKeyError(
            'DuplicatedKeyError: {} is already in the tree'.format(key)
        )
