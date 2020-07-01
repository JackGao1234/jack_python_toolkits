def transform(input_data: list):
    return [i * 2 - 1 for i in input_data if type(i) is not str]
