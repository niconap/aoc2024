import numpy as np

with open('./input.txt', 'r') as f:
    lines = f.readlines()

first_list = np.zeros(len(lines))
second_list = np.zeros(len(lines))
for i, line in enumerate(lines):
    parts = line.split('   ')
    first_list[i] = int(parts[0].strip())
    second_list[i] = int(parts[1].strip())

unique, counts = np.unique(second_list, return_counts=True)
count_dict = dict(zip(unique, counts))
score = 0
for item in first_list:
    if item in count_dict:
        score += item*count_dict[item]

print(int(score))