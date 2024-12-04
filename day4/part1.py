import numpy as np
import re


def create_matrix(lines):
    matrix = []
    for line in lines:
        line = line.strip()
        row = []
        for letter in line:
            row.append(letter)
        matrix.append(row)

    return np.array(matrix)


def search_rows(matrix):
    total = 0
    for row in matrix:
        string = ''.join(row.astype(str))
        front = re.findall('XMAS', string)
        back = re.findall('SAMX', string)
        total += len(front) + len(back)
    return total


def search_cols(matrix):
    matrix = matrix.T
    total = 0
    for row in matrix:
        string = ''.join(row.astype(str))
        front = re.findall('XMAS', string)
        back = re.findall('SAMX', string)
        total += len(front) + len(back)
    return total


def search_diags(matrix):
    # Search in both left to right and right to left
    # start at bl
    total = 0

    offsets = matrix.shape
    for i in range(-offsets[0], offsets[1]):
        row = np.diagonal(matrix, offset=i)
        string = ''.join(row.astype(str))
        front = re.findall('XMAS', string)
        back = re.findall('SAMX', string)
        total += len(front) + len(back)

    matrix = matrix[:, ::-1]
    for i in range(-offsets[0], offsets[1]):
        row = np.diagonal(matrix, offset=i)
        string = ''.join(row.astype(str))
        front = re.findall('XMAS', string)
        back = re.findall('SAMX', string)
        total += len(front) + len(back)

    return total


with open('./input.txt', 'r') as f:
    lines = f.readlines()

matrix = create_matrix(lines)
row_amount = search_rows(matrix)
col_amount = search_cols(matrix)
diag_amount = search_diags(matrix)
print(row_amount + col_amount + diag_amount)
