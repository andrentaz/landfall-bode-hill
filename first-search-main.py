# -*- encoding: utf-8 -*-
"""
This is a simple driver program to make use of the graph and helpers modules to
implement any First Search algorithm.

The program run with some args to get the graph and the starting node.
"""
import argparse

from graph import Graph


def main(filename, start, search):
    """Get the search from start node in a given graph"""
    v_start = None
    graph = Graph()


    try:
        graph.create_from_file(filename)
    except IndexError:
        print('Something wrong with the adjacency list: {}'.format(filename))
        print('Tried to create edge between non existing vertexes')
        return

    try:
        v_start = graph.vertexes[start]
    except IndexError:
        print('Non existing start: ({})'.format(start))
        return

    if search == 'bfs':
        search_tree = graph.breadth_first_search(v_start)
    elif search == 'dfs':
        search_tree = graph.depth_first_search(v_start)
    else:
        print("Unknown search first type, valid values are 'bfs' or 'dfs'")
        return

    print()
    print("Runned {} algorithm on '{}'".format(search.upper(), filename))
    print('Resume - Vertexes: {}, Tree Edges: {}' \
        .format(len(graph.vertexes), len(search_tree)))
    print('Tree: {}'.format(search_tree))
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
    parser.add_argument('search',
                        help='type of search bfs|dfs',
                        type=str)
    args = parser.parse_args()

    # call main function
    main(
        filename=args.filename,
        start=args.start,
        search=args.search,
    )
