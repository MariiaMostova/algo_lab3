from collections import defaultdict


class Graph:
    def __init__(self, v_count):
        self.graph = defaultdict(list)
        self.v_count = v_count

    def __del__(self):
        pass

    def add_edge(self, u, v_count):
        self.graph[u].append(v_count)

    def recursive_dnf(self, v_count, visited_v, v_stack, cycle):
        visited_v[v_count] = True
        v_stack[v_count] = True
        for edge_v in self.graph[v_count]:
            if not visited_v[edge_v]:
                if self.recursive_dnf(edge_v, visited_v, v_stack, cycle):
                    cycle.append(edge_v)
                    return True
            elif v_stack[edge_v]:
                cycle.append(edge_v)
                return True
        v_stack[v_count] = False
        return False

    def detect_cycle(self):
        visited_v = [False for i in range(self.v_count)]
        v_stack = [False for i in range(self.v_count)]
        cycle = []
        for node in range(self.v_count):
            if not visited_v[node]:
                if self.recursive_dnf(node, visited_v, v_stack, cycle):
                    return cycle
        return False
