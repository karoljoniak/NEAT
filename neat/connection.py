class Connection:
    def __init__(self, input_id, output_id, weight, enabled, innovation):
        self.input_id = input_id
        self.output_id = output_id
        self.weight = weight
        self.enabled = enabled
        self.innovation = innovation

    def __str__(self):
        return f'In: {self.input_id}, Out: {self.output_id}, Weight: {self.weight}, Enabled: {self.enabled}, Innov: {self.innovation}'
