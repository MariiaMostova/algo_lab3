from collections import defaultdict


class Graph:
    def __init__(self, count):
        self.graph = defaultdict(list)
        self.count = count

    def __del__(self):
        pass

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def recursive_dfs(self, v, visited_v, v_stack, cycle):
        visited_v[v] = True
        v_stack[v] = True
        for edge_v in self.graph[v]:
            if not visited_v[edge_v] and self.recursive_dfs(edge_v, visited_v, v_stack, cycle):
                cycle.append(edge_v)
                return True
            elif v_stack[edge_v]:
                cycle.append(edge_v)
                return True
        v_stack[v] = False
        return False

    def detect_cycle(self):
        visited_v = [False for i in range(self.count)]
        v_stack = [False for i in range(self.count)]
        cycle = []
        for node in range(self.count):
            if not visited_v[node]:
                if self.recursive_dfs(node, visited_v, v_stack, cycle):
                    return cycle
        return False
