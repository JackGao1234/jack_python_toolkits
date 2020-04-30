import json

input_data = [i for i in range(1000)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ... 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]
expected_output = [i for i in range(-1, 1998, 2)]
# [-1, 1, 3, 5, 7, 9, 11, 13, 15, 17 ... 1979, 1981, 1983, 1985, 1987, 1989, 1991, 1993, 1995, 1997]

print(input_data[:10], "...", input_data[-10:])
print(expected_output[:10], "...", expected_output[-10:])

# print('\n'.join([str(element) for element in input_data]))

with open("data_input", 'w+') as f:
    json.dump(input_data, f)

with open("data_output_expected", 'w+') as f:
    json.dump(expected_output, f)
