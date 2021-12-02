DFS = 0
BFS = 0


class Graph(object):
    def __init__(self, graph=None):
        if graph is None:
            graph = {}
        self.graph = graph
        self.visited = set()
        self.queue = []
        self.bfs_queue = []

    def get_first_vertex(self):
        return list(self.graph.keys())[0]

    def clear_visited(self):
        self.visited = set()

    def clear_bfs_queue(self):
        self.bfs_queue = []

    def add_edge(self, edge):
        edge = set(edge)
        v1, v2 = tuple(edge)
        for x, y in [(v1, v2), (v2, v1)]:
            if x in self.graph:
                self.graph[x].append(y)
            else:
                self.graph[x] = [y]

    def __iter__(self):
        self.iter_obj = iter(self.graph)
        return self.iter_obj

    def __next__(self):
        return next(self.iter_obj)

    def dfs(self, vertex):
        global DFS
        if vertex in self.visited:
            return
        self.visited.add(vertex)
        self.bfs_queue.append(vertex)
        DFS += 1
        for i in self.graph[vertex]:
            if i not in self.visited:
                self.dfs(i)

    def bfs(self, vertex):
        global BFS
        if vertex in self.visited:
            return
        self.visited.add(vertex)
        BFS += 1
        self.bfs_queue.append(vertex)
        for i in self.graph[vertex]:
            if i not in self.visited:
                self.queue.append(i)
        while self.queue:
            self.bfs(self.queue.pop(0))

    def get_visited(self):
        return self.visited

    def get_bfs_queue(self):
        return self.bfs_queue


matrix = []
with open('tasks/z7/input.txt') as f:
    for line in f:
        matrix.append(list(map(int, line.split())))
graph = Graph()
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph.add_edge({i, j})
graph.dfs(graph.get_first_vertex())
print(graph.get_bfs_queue())
graph.clear_bfs_queue()
graph.clear_visited()
graph.bfs(graph.get_first_vertex())
print(graph.get_bfs_queue())
with open('tasks/z7/output.txt', 'w') as f:
    f.write(f'DFS {DFS}\nBFS {BFS}')
