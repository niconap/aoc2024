import numpy as np

with open('./input.txt', 'r') as f:
    lines = f.readlines()

first_list = np.zeros(len(lines))
second_list = np.zeros(len(lines))
for i, line in enumerate(lines):
    parts = line.split('   ')
    first_list[i] = int(parts[0].strip())
    second_list[i] = int(parts[1].strip())

first_sorted = np.sort(first_list)
second_sorted = np.sort(second_list)

distances = np.abs(first_sorted - second_sorted)
print(int(np.sum(distances)))
