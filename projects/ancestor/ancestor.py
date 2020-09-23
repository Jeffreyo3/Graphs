from util import *
from graph import Graph

# Describe the problem in graphs terminology
## What are our nodes? numbers/people
## What are our edges? if a descendant/parent
## Directed graph

# Build your graph or write getNeighbors()
## Can do either

# Choose your fighter!
## Which algorithm in this situation?
### BFS, DFS, BFT, DFT

## Search or a traversal?
## More like a traversal: visit every possible from your starting node

## Depth vs Breadth
## BF --> shortest path
## DF --> heads to leaves first

## DF can be recursive, but not BF
 

def earliest_ancestor(ancestors, starting_vertex):
    graph = Graph()

    ## iterate over all ancestors, 
    for an in ancestors:
        # add each node to the graph
        # (parent, child)
        graph.add_vertex(an[0])
        graph.add_vertex(an[1])
        ## add each edge to the graph
        graph.add_edge(an[1], an[0])
    
    ## run a traversal​

    # make a queue
    q = Queue()
    # initialize with first vertex
    q.enqueue(starting_vertex)
    # make a set to track visited vertex
    visited = set()
    
    end_vertex = []

    while q.size() > 0:
        # print(end_vertex)
        end_vertex = []
        curr_vertex = q.dequeue()

        if curr_vertex not in visited:
            # print(curr_vertex)
            visited.add(curr_vertex)
            neighbors = graph.get_neighbors(curr_vertex)

            for neighbor in neighbors:
                neighbor_neighbors = graph.get_neighbors(neighbor)

                if neighbor_neighbors:
                    q.enqueue(neighbor)
                else:
                    end_vertex.append(neighbor)
    
    
    if len(end_vertex) > 0:
        # return sorted(end_vertex)[0]
        end_vertex.sort()
        return(end_vertex[0])
    return -1
    