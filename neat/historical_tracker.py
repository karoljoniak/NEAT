from neat.node import Node


class HistoricalTracker:
    innovation: int = 0
    node_id: int = 0
    new_nodes_tracker: list = []
    new_connections_tracker: list = []

    @staticmethod
    def inc_innovation() -> None:
        HistoricalTracker.innovation = HistoricalTracker.innovation + 1

    @staticmethod
    def inc_node_id() -> None:
        HistoricalTracker.node_id = HistoricalTracker.node_id + 1

    @staticmethod
    def add_node_to_history(node_id, input_node_id, output_node_id):
        HistoricalTracker.new_nodes_tracker.append(
            {"id": node_id, "input": input_node_id, "output": output_node_id})

    @staticmethod
    def clear_nodes_tracker():
        HistoricalTracker.new_nodes_tracker.clear()

    @staticmethod
    def search_for_duplicated_node(input_node_id, output_node_id):
        for item in HistoricalTracker.new_nodes_tracker:
            if item["input"] == input_node_id and item["output"] == output_node_id:
                return item
        return None

    @staticmethod
    def add_connection_to_history(innovation, input_node_id, output_node_id):
        HistoricalTracker.new_connections_tracker.append(
            {"innovation": innovation, "input": input_node_id, "output": output_node_id})

    @staticmethod
    def search_for_duplicated_connections(input_node_id, output_node_id):
        for item in HistoricalTracker.new_connections_tracker:
            if item["input"] == input_node_id and item["output"] == output_node_id:
                return item
        return None

    @staticmethod
    def print_nodes_history():
        print("NODE TRACKER")
        for item in HistoricalTracker.new_nodes_tracker:
            print(item)

    @staticmethod
    def print_connections_history():
        print("CONNECTIONS TRACKER")
        for item in HistoricalTracker.new_connections_tracker:
            print(item)
