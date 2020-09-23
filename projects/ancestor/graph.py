"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("Error: Vertext does not exist")
            return None


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # initialize with first vertex
        q.enqueue(starting_vertex)
        # make a set to track visited vertex
        visited = set()

        while q.size() > 0:
            curr_vertex = q.dequeue()

            if curr_vertex not in visited:
                print(curr_vertex)
                visited.add(curr_vertex)
                neighbors = self.get_neighbors(curr_vertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack of vertex to visit
        s = Stack()
        # initialize with first vertex
        s.push(starting_vertex)
        # make a set to track visited vertex
        visited = set()

        while s.size() > 0:
            curr_vertex = s.pop()

            if curr_vertex not in visited:
                print(curr_vertex)
                visited.add(curr_vertex)
                neighbors = self.get_neighbors(curr_vertex)
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        visited.add(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        visited = set()
        path = []

        vertices = self.vertices

        q.enqueue(starting_vertex)

        while q.size() > 0:
            curr_vertex = q.dequeue()

            visited.add(curr_vertex)
            path.append(curr_vertex)

            if curr_vertex == destination_vertex:
                return path

            for vertex in vertices[curr_vertex]:
                if vertex not in visited:
                    neighbors = self.get_neighbors(vertex)

                    if destination_vertex in neighbors:
                        path.append(vertex)
                        path.append(destination_vertex)
                        return path
                    
                    q.enqueue(vertex)
        
        return "Error: No valid path"



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        vertices = self.vertices
        
        path = [starting_vertex]

        while s.size() > 0:
            # remove from stack
            curr_vertex = s.pop()
            # print(curr_vertex)
            # end function & return path if current is destination
            if curr_vertex == destination_vertex:
                visited.add(curr_vertex)
                path.append(curr_vertex)
                return path

            # if we haven't visited current yet, do stuff
            if curr_vertex not in visited:
                # add to visited set
                visited.add(curr_vertex)

                # go through keys in verticies and 
                for vertex in vertices[curr_vertex]:
                    s.push(vertex)

                    if vertex not in visited:
                        neighbors = self.get_neighbors(vertex)
                        if destination_vertex in neighbors:
                            path.append(curr_vertex)
                            path.append(vertex)
                            path.append(destination_vertex)
                            
                            return path
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # add starting to visited set
        visited.add(starting_vertex)
        
        path = path + [starting_vertex]
        print(path)
        if starting_vertex == destination_vertex:
            return path

        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
