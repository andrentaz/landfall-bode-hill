# -*- encoding: utf-8 -*-
"""
This module contains all the auxiliar data structures and functions required to
implement Dijkstra's algorithm.

:author: Andre Filliettaz
:email: andrentaz@gmail.com
:github: https://github.com/andrentaz
"""
from __future__ import absolute_import, unicode_literals


class BinaryMinHeap(object):
    """A simple implementation of a BinaryMinHeap"""
    def __init__(self, heap):
        super(BinaryMinHeap, self).__init__()
        self.heap = heap

    def __repr__(self):
        return (
            'BinaryMinHeap(size={}, '
            'min={}, '
            'heap={})'
        ).format(len(self.heap), self.heap[0], self.heap)

    def min_heapify(self, idx):
        # total array size
        length = len(self.heap) - 1

        # indexes
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx

        if left <= length and self.heap[idx] > self.heap[left]:
            smallest = left

        if right <= length and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self.min_heapify(smallest)

    def build_min_heap(self):
        array = self.heap
        for i in reversed(range(len(array)//2)):
            self.min_heapify(i)

    def extract_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        minimum = self.heap.pop()
        self.build_min_heap()

        return minimum
