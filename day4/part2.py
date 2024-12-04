import numpy as np


def create_matrix(lines):
    matrix = []
    for line in lines:
        line = line.strip()
        row = []
        for letter in line:
            row.append(letter)
        matrix.append(row)

    return np.array(matrix)


def find_x_mas(matrix):
    total = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if matrix[i, j] == 'A':
                if matrix[i - 1, j - 1] == 'M' and matrix[i + 1, j + 1] == 'S':
                    if matrix[i + 1, j - 1] == 'M' and matrix[i - 1, j + 1] == 'S':
                        total += 1
                    if matrix[i + 1, j - 1] == 'S' and matrix[i - 1, j + 1] == 'M':
                        total += 1
                if matrix[i - 1, j - 1] == 'S' and matrix[i + 1, j + 1] == 'M':
                    if matrix[i + 1, j - 1] == 'M' and matrix[i - 1, j + 1] == 'S':
                        total += 1
                    if matrix[i + 1, j - 1] == 'S' and matrix[i - 1, j + 1] == 'M':
                        total += 1
    return total


with open('./input.txt', 'r') as f:
    lines = f.readlines()

matrix = create_matrix(lines)
count = find_x_mas(matrix)
print(count)
