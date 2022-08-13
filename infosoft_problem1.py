# Problem 1 - Data Stream Ingestion


class DataStream:
    """
    We are gonna use a dictionary where the data string will be our key
    and we will keep track of the the time in value against that particular key.
    """
    def __init__(self):
        self.print_string = {}

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
        # if the string is not in the dictionary then we will add it into dictionary
        if data_string not in self.print_string:
            self.print_string[data_string] = timestamp
            return True

        if timestamp - self.print_string[data_string] >= 5:
            self.print_string[data_string] = timestamp
            return True

        else:
            return False


data_stream = DataStream()
output1 = data_stream.should_output_data_str(timestamp=0, data_string="hello")
print(output1)
output2 = data_stream.should_output_data_str(timestamp=1, data_string="world")
print(output2)
output3 = data_stream.should_output_data_str(timestamp=6, data_string="hello")
print(output3)
output4 = data_stream.should_output_data_str(timestamp=7, data_string="hello")
print(output4)
output5 = data_stream.should_output_data_str(timestamp=8, data_string="world")
print(output5)
