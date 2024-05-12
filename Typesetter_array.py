import numpy as np

with open('Data_random_p_1_80.txt', 'r') as file:
    lines = [line.strip('[\]\n').split(', ') for line in file.readlines()]

data = np.array([[float(x) for x in line] for line in lines])

formatted_data = ', '.join([f'[{", ".join(map(str, row))}]' for row in data])

print(f'[{formatted_data}]')
