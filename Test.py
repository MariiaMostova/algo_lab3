import unittest
from DFS import Graph


def create_graph(file_name):
    with open(file_name) as file:
        num = file.readline()
        graph = Graph(int(num))
        for line in file.readlines():
            edge = line.split(" ")
            u = int(edge[0])
            v = int(edge[1])
            graph.add_edge(u, v)
    return graph


class Test1(unittest.TestCase):
    def test_no_cycle(self):
        g = create_graph('test_no_cycle.txt')
        g_new = g.detect_cycle()
        self.assertEqual(g_new, False)


class Test2(unittest.TestCase):
    def test_small_graph(self):
        g = create_graph('test_small_graph.txt')
        g_new = g.detect_cycle()
        self.assertEqual(g_new, [0, 5, 10])


class Test3(unittest.TestCase):
    def test_big_graph(self):
        g = create_graph('test_big_graph.txt')
        g_new = g.detect_cycle()
        self.assertEqual(g_new, [46, 70, 73, 163, 125, 98, 20, 127, 131, 154, 46, 62, 167])


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(Test1())
    runner.run(Test2())
    runner.run(Test3())
