# -*- encoding: utf-8 -*-
"""
A program that implements dijkstras algorithm for shortest path

:author: Andre Filliettaz
:email: andrentaz@gmail.com
:github: https://github.com/andrentaz
"""
from __future__ import absolute_import, unicode_literals

import sys


class Edge:
    """Implements an abstractio to graph's Edge"""
    def __init__(self, neighboor, distance):
        self.neighboor = neighboor
        self.distance = distance

    def __repr__(self):
        return (
            'Edge(neighboor={}, '
            'distance={})'
        ).format(
            self.neighboor.label,
            self.distance,
        )


class Vertex:
    """Implements an abstraction to graph's Vertex"""
    def __init__(self, label, distance=sys.maxint):
        self.label = label
        self.distance = distance
        self.edges = []
        self.visited = False

    def __repr__(self):
        return (
            'Vertex(label={}, '
            'distance={}, '
            'edges={}, '
            'visited={})'
        ).format(
            self.label,
            self.distance,
            len(self.edges),
            self.visited,
        )

    def add_edge(self, vertex, dist):
        self.edges.append(Edge(vertex, dist))


class Graph:
    """Implements an abstraction to Graphs using a list of vertexes"""
    def __init__(self):
        self.vertexes = []

    def __repr__(self):
        return ('Graph(vertexes={})').format(len(self.vertexes))

    def create_from_file(self, number_of_vertexes, filename):
        """Create a graph from a file with a matrix of distances"""

        # initialize the vertex list
        for i in range(number_of_vertexes):
            self.vertexes.append(Vertex(str(i)))

        # read matrix of distances from file
        with open(filename, 'r') as file:
            for from_idx, row in enumerate(file):
                for to_idx, column in enumerate(row.split(' ')):
                    dist = int(column.rstrip('\n'))

                    if not dist > 0:
                        continue

                    v_from = self.vertexes[from_idx]
                    v_to = self.vertexes[to_idx]

                    v_from.add_edge(v_to, dist)
