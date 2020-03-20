# -*- coding: utf-8 -*-


class Tree(object):
    """An abstraction to the Balanced Tree"""

    class DuplicatedKeyError(Exception):
        """Trees don't allow duplicated keys"""
        pass

    def __init__(self, key=None, parent=None):
        """Creates an empty tree"""
        super(Tree, self).__init__()
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        return(
            'Tree(key={}, '
            'left={}, '
            'right={}, '
            'parent={})'
        ).format(
            self.key,
            self.left.key if self.left else None,
            self.right.key if self.right else None,
            self.parent.key if self.parent else None,
        )

    def is_leaf(self):
        return self.left is None and self.right is None

    def insert(self, key):
        """Implements Tree insertion recursively"""
        if not self.key:
            self.key = key
            return self

        if self.key > key:
            if not self.left:
                self.left = Tree(key, self)
                return self.left
            else:
                return self.left.insert(key)

        if self.key < key:
            if not self.right:
                self.right = Tree(key, self)
                return self.right
            else:
                return self.right.insert(key)

        raise DuplicatedKeyError(
            'DuplicatedKeyError: {} is already in the tree'.format(key)
        )

    def search(self, key):
        """Implements Tree search recursively"""
        if self.key == key:
            return self

        if self.key > key:
            if not self.left:
                return None
            else:
                return self.left.search(key)

        if not self.right:
            return None
        else:
            return self.right.search(key)

    def get_max(self):
        target = self
        while target.right:
            target = target.right
        return target

    def get_min(self):
        target = self
        while target.left:
            target = target.left
        return target

    def remove(self, key):
        """Implements Tree removal recursively"""

        # Base case for leaf
        if self.is_leaf():
            if self.key == key:
                return None
            return self

        # search for key to be removed
        if key < self.key:
            if self.left:
                self.left = self.left.remove(key)
            else:
                return self
        elif key > self.key:
            if self.right:
                self.right = self.right.remove(key)
            else:
                return self

        # found the key
        else:
            # check for incomplete root
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # complete root
            else:
                new_root = self.right.get_min()
                self.key = new_root.key
                self.right = self.right.remove(new_root.key)

        return self
