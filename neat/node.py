class Node:
    def __init__(self, node_id, node_type, input_node_id=None, output_node_id=None):
        if input_node_id is None:
            input_node_id = list()
        self.__id = node_id
        self.__type = node_type
        self.__input_node_id = input_node_id
        self.__output_node_id = output_node_id

    def __str__(self):
        return f'ID: {self.get_id()}, TYPE: {self.get_type()} CONN: {self.get_input_node_id()}->{self.get_output_node_id()}'

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def get_input_node_id(self):
        return self.__input_node_id

    def get_output_node_id(self):
        return self.__output_node_id

    def set_input_node_id(self, __id: int):
        if __id not in self.__input_node_id:
            self.__input_node_id.append(__id)

    def set_output_node_id(self, __id: int):
        self.__output_node_id = __id
