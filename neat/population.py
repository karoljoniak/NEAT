from neat.genome import Genome
from neat.historical_tracker import HistoricalTracker
from neat.geneticOperators import mutate_add_node


class Population:
    def __init__(self, quantity: int, sensors: int, outputs: int):
        self.individuals = [Genome(input_number=sensors, output_number=outputs) for _ in range(quantity)]
        HistoricalTracker.innovation = sensors * outputs - 1
        HistoricalTracker.node_id = sensors + outputs - 1

        for _individual in self.individuals:
            mutate_add_node(_individual)

        HistoricalTracker.print_nodes_history()
        HistoricalTracker.print_connections_history()

    def __str__(self):
        for _individual in self.individuals:
            print('/*****************INDIVIDUAL**************************/')
            print(_individual, end='')
            print('/*****************************************************/', end='\n\n')
        return ''
