class GetUniqueIdentifier:
    # here we set the most significant number the very left one
    def __init__(self, block_size: int = 10):
        self.data_to_calculate: list[int] = None
        self.block_size: int = block_size
        self.unique_identifier: int = None

    def fill_data(self, data: list[int]):
        self.data_to_calculate = data

    def calculate_unique_identifier(self):
        identifier_sum = 0
        for number in self.data_to_calculate:
            identifier_sum = (number + identifier_sum) * self.block_size
        self.unique_identifier = int(identifier_sum / self.block_size)


if __name__ == "__main__":
    worker = GetUniqueIdentifier(8)
    worker.fill_data([2, 4, 5])
    worker.calculate_unique_identifier()
    print(worker.unique_identifier)
