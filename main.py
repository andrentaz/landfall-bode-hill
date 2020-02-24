# -*- encoding: utf-8 -*-
"""
This is a simple driver program to make use of the graph and helpers modules to
implement Dijkstra's Algorithm for find the shortest path between some nodes.

The program run with some args to get the graph, the starting node and maybe the
end node. If no end node is provided, the algorithm will run over all the nodes
in the graph, calculating the shortest path tree (SPT).
"""
import argparse

from graph import Graph


def main(filename, start, **kwargs):
    v_start = None
    v_end = None
    graph = Graph()

    end = kwargs.get('end', None)

    try:
        graph.create_from_file(filename)
    except IndexError:
        print('Something wrong with the adjacency matrix: {}'.format(filename))
        print('Tried to create edge between non existing vertexes')
        return

    try:
        v_start = graph.vertexes[start]

        if end:
            v_end = graph.vertexes[end]
    except IndexError:
        print('Non existing start or end: ({}, {})'.format(start, end))
        return

    path = graph.path(v_start, v_end, run_dijkstra=True)
    path_nodes = ' -> '.join([n.label for n in path.get('path')])

    print()
    print("Runned Dijkstra's algorithm on '{}'".format(filename))
    print('Resume - Vertexes: {}, Path Nodes: {}, Distance: {}' \
        .format(len(graph.vertexes), path_nodes, path.get('distance')))
    print('Path: {}'.format(path))
    print()



if __name__ == '__main__':
    # handle script arguments
    parser = argparse.ArgumentParser(
        description='Calculate shortest path on graphs.'
    )
    parser.add_argument('filename',
                        help='path to the file containing the adjacency list')
    parser.add_argument('start',
                        help='starting node index',
                        type=int)
    parser.add_argument('-e',
                        '--end',
                        help='ending node index',
                        type=int)
    args = parser.parse_args()

    # call main function
    main(
        filename=args.filename,
        start=args.start,
        end=args.end,
    )
