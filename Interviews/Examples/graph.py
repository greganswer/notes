class Graph:
    def __init__(self):
        self.node_count = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if self.adjacent_list.get(node) is None:
            self.adjacent_list[node] = set()
            self.node_count += 1

    def add_edge(self, node1, node2):
        if self.adjacent_list.get(node1) is None:
            return
        list = self.adjacent_list
        if list.get(node1) is not None and list.get(node2) is not None:
            self.adjacent_list[node1].add(node2)
            self.adjacent_list[node2].add(node1)

    def show_connections(self):
        output = ''
        for node, vertices in self.adjacent_list.items():
            output += f"{node} --> {' '.join(vertices)}\n"
        return output


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('3', '1')
graph.add_edge('3', '4')
graph.add_edge('4', '2')
graph.add_edge('4', '5')
graph.add_edge('1', '2')
graph.add_edge('1', '0')
graph.add_edge('0', '2')
graph.add_edge('6', '5')
print(graph.show_connections())

