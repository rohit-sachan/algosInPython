from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self, connections, directed=True):
        self._adj = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._adj[node1].add(node2)
        if not self._directed:
            self._adj[node2].add(node1, )

    def get_adj(self, node):
        return self._adj[node]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._adj))


class GraphWeighted:
    def __init__(self, connections, directed=True):
        self._adj = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2, wt in connections:
            self.add(node1, node2, wt)

    def add(self, node1, node2, wt):
        self._adj[node1].add((node2, wt))
        if not self._directed:
            self._adj[node2].add(node1, wt)

    def get_adj(self, node):
        return self._adj[node]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._adj))

    def find_path_bfs(self, node1, node2):  # path for fewest intermediate transactions
        visited = set()  # to keep track and save from multiple visits
        tracker = dict()
        q = Queue()
        q.put(node1)
        while not q.empty():
            source = q.get()
            neighbours = self.get_adj(source)

            for node in neighbours:
                print(node)
                if not visited.__contains__(node):
                    q.put(node[0])
                    tracker[node[0]] = source
                if node[0] == node2:
                    return self.create_path(tracker, node1, node2)

    @staticmethod
    def create_path(tracker, node_s, node_d):
        path = list()
        node_t = None
        while node_t != node_s:
            node_t = tracker[node_d]
            path.append(node_d)
            node_d = node_t

