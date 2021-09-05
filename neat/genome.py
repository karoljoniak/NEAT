# packages
from random import uniform

# neat
from neat.graphics import show_ann_as_graph
from neat.connection import Connection
from neat.node import Node
from neat.geneType import GeneTypes


class Genome:
    def __init__(self, input_number, output_number):
        self.fitness = 0.0
        self.input_nodes = [Node(node_id=x, node_type=GeneTypes.SENSOR) for x in range(input_number)]
        self.output_nodes = [Node(node_id=x, node_type=GeneTypes.OUTPUT) for x in
                             range(input_number, input_number + output_number)]
        self.hidden_nodes = []
        self.connections = []

        innovation = 0

        for input_node in self.input_nodes:
            for output_node in self.output_nodes:
                # making nodes aware of their connections
                input_node.set_output_node_id(output_node.get_id())
                output_node.set_input_node_id(input_node.get_id())

                # creating connection instances
                self.connections.append(
                    Connection(input_id=input_node.get_id(), output_id=output_node.get_id(), weight=uniform(-1, 1),
                               enabled=True,
                               innovation=innovation))

                innovation = innovation + 1

    def __str__(self):
        for _input in self.input_nodes:
            print(_input)
        for _output in self.output_nodes:
            print(_output)
        for _hidden in self.hidden_nodes:
            print(_hidden)

        print(end="\n\n")
        for _connection in self.connections:
            print(_connection)
        return ''

    def display(self):
        connections = []
        nodes = []
        for node in self.input_nodes:
            nodes.append(node.get_id())
        for node in self.hidden_nodes:
            nodes.append(node.get_id())
        for node in self.output_nodes:
            nodes.append(node.get_id())

        for connection in self.connections:
            connections.append((connection.input_id, connection.output_id))

        show_ann_as_graph(nodes, connections)
