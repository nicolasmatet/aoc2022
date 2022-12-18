import re
from collections import defaultdict

regex = re.compile('Valve ([A-Z]+) has flow rate=([0-9]+); tunnel[s]? lead[s]? to valve[s]? (.+)')
FLOW = 'flow_rate'
OPEN_VALVE = 'open'
ACHIEVEMENT = 'acheivement'


def lines():
    for line in open("input.txt"):
        valve_id, flow_rates, neighbors = re.match(regex, line).groups()
        yield valve_id, int(flow_rates), neighbors.replace(" ", '').split(',')


class Graph:
    def __init__(self, is_digragh=True):
        self.nodes = dict()
        self.out_edges = defaultdict(set)
        self.in_edges = defaultdict(set)
        self.is_digragh = is_digragh

    def add_node(self, node_id, new_props=None):
        if node_id in self.nodes:
            old_props = self.nodes[node_id]
        else:
            old_props = dict()
        if new_props:
            old_props.update(new_props)
        self.nodes[node_id] = old_props

    def add_edge(self, from_node, to_node):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)

        self.out_edges[from_node].add(to_node)
        if self.is_digragh:
            self.in_edges[to_node].add(from_node)

    def clone(self):
        new_graph = Graph()
        new_graph.in_edges = self.in_edges
        new_graph.out_edges = self.out_edges
        new_graph.nodes = {**self.nodes}
        return new_graph


def build_graph():
    graph = Graph()
    for node_id, flow_rate, neighbors in lines():
        graph.add_node(node_id, {FLOW: flow_rate, OPEN_VALVE: False})
        for neigh in neighbors:
            graph.add_edge(node_id, neigh)
    return graph


def open_valve(graph, current_node, max_steps, current_flow, flow_map):
    graph.nodes[current_node][OPEN_VALVE] = True
    return crawl(graph, current_node, max_steps - 1, current_flow, flow_map)


def go_to_neighbor(neighbor):
    def wrapper(graph, current_node, max_steps, current_flow, flow_map):
        graph.nodes[neighbor][current_node] = True
        return crawl(graph, neighbor, max_steps - 1, current_flow, flow_map)
    return wrapper


def crawl(graph, current_node, max_steps, current_flow, flow_map):
    new_graph = graph.clone()
    if current_flow < flow_map[current_node][0] and max_steps < flow_map[current_node][1]:
        return 0
    if current_flow > flow_map[current_node][0] and max_steps > flow_map[current_node][1]:
        flow_map[current_node] = (current_flow, max_steps)

    if max_steps == 0:
        return 0
    actions = []
    if not new_graph.nodes[current_node][OPEN_VALVE] and new_graph.nodes[current_node][FLOW]:
        actions.append(open_valve)
    for neighbor in sorted(new_graph.out_edges[current_node]):
        if current_node not in new_graph.nodes[neighbor]:  # neighbor was already visited from this node
            actions.append(go_to_neighbor(neighbor))
    if not actions:
        return 0
    current_flow = sum(n[FLOW] for n in graph.nodes.values() if n[OPEN_VALVE])
    max_pressure_relieved = 0
    for action in actions:
        pressure_relieved = action(new_graph, current_node, max_steps, current_flow, flow_map) + current_flow
        max_pressure_relieved = max(max_pressure_relieved, pressure_relieved)
    return max_pressure_relieved


def solve1():
    graph = build_graph()
    pressure_relieved = crawl(graph, 'AA', 30, 0, defaultdict(lambda:(0, 0)))
    return pressure_relieved


def solve2():
    pass


if __name__ == "__main__":
    print(solve1())
    print(solve2())
