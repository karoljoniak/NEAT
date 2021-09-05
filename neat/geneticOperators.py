# packages
from random import randint

# neat
from neat.node import Node
from neat.geneType import GeneTypes
from neat.connection import Connection
from neat.genome import Genome
from neat.historical_tracker import HistoricalTracker


def mutate_add_connection(genome: Genome) -> None:
    pass


def mutate_add_node(genome: Genome) -> None:
    # picking random connection, where new node will be added (trying to pick until connection is enabled)
    while True:
        connection_idx = randint(0, len(genome.connections) - 1)
        connection = genome.connections[connection_idx]
        if not connection.enabled:
            continue
        else:
            connection.enabled = False
            break

    # checking if new node was added in that place in the past
    existing_node = HistoricalTracker.search_for_duplicated_node(input_node_id=connection.input_id,
                                                                 output_node_id=connection.output_id)

    # adding new node
    if existing_node:
        new_node = Node(existing_node["id"], GeneTypes.HIDDEN)
        new_node_id = existing_node["id"]

    else:
        HistoricalTracker.inc_node_id()
        new_node_id = HistoricalTracker.node_id
        new_node = Node(new_node_id, GeneTypes.HIDDEN)
        HistoricalTracker.add_node_to_history(new_node_id, connection.input_id, connection.output_id)

    # making new node aware of its connections (needed for history tracking)
    new_node.set_input_node_id(connection.input_id)
    new_node.set_output_node_id(connection.output_id)

    # adding node to neural net
    genome.hidden_nodes.append(new_node)

    # checking if that input connection already exists in history tracker
    existing_connection = HistoricalTracker.search_for_duplicated_connections(input_node_id=connection.input_id,
                                                                              output_node_id=new_node_id)
    # adding new node input connection to neural net
    if existing_connection:
        new_connection_1 = Connection(input_id=connection.input_id, output_id=new_node_id, enabled=True,
                                      weight=connection.weight, innovation=existing_connection["innovation"])
    else:
        HistoricalTracker.inc_innovation()
        new_innovation_num = HistoricalTracker.innovation
        new_connection_1 = Connection(input_id=connection.input_id, output_id=new_node_id, enabled=True,
                                      weight=connection.weight, innovation=new_innovation_num)
        HistoricalTracker.add_connection_to_history(new_innovation_num, connection.input_id, new_node_id)

    genome.connections.append(new_connection_1)

    # checking if that output connection already exists in history tracker
    existing_connection = HistoricalTracker.search_for_duplicated_connections(input_node_id=new_node_id,
                                                                              output_node_id=connection.output_id)

    # adding new node output connection to neural net
    if existing_connection:
        new_connection_2 = Connection(input_id=new_node_id, output_id=connection.output_id, enabled=True,
                                      weight=connection.weight, innovation=existing_connection["innovation"])
    else:
        HistoricalTracker.inc_innovation()
        new_innovation_num = HistoricalTracker.innovation
        new_connection_2 = Connection(input_id=new_node_id, output_id=connection.output_id, enabled=True,
                                      weight=connection.weight, innovation=new_innovation_num)
        HistoricalTracker.add_connection_to_history(new_innovation_num, new_node_id, connection.output_id)
    genome.connections.append(new_connection_2)


def crossover():
    pass
