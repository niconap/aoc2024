with open('./input.txt', 'r') as f:
    lines = f.readlines()


def go_hor(matrix, pos, step):
    end_found = False
    while pos[1] + step >= 0 and pos[1] + step < len(matrix[0]):
        if matrix[pos[0]][pos[1] + step] == '#':
            matrix[pos[0]][pos[1]] = 'X'
            break
        matrix[pos[0]][pos[1]] = 'X'
        pos[1] += step
    if pos[1] + step < 0 or pos[1] + step >= len(matrix[0]):
        matrix[pos[0]][pos[1]] = 'X'
        end_found = True
    return matrix, pos, end_found


def go_ver(matrix, pos, step):
    end_found = False
    while pos[0] + step >= 0 and pos[0] + step < len(matrix):
        if matrix[pos[0] + step][pos[1]] == '#':
            matrix[pos[0]][pos[1]] = 'X'
            break
        matrix[pos[0]][pos[1]] = 'X'
        pos[0] += step
    if pos[0] + step < 0 or pos[0] + step >= len(matrix):
        matrix[pos[0]][pos[1]] = 'X'
        end_found = True
    return matrix, pos, end_found


def walk(matrix):
    pos = None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '^':
                pos = [i, j]

    ver = True
    step = -1
    end_found = False
    while not end_found:
        if ver:
            matrix, pos, end_found = go_ver(matrix, pos, step)
            ver = False
            step *= -1
        elif not ver:
            matrix, pos, end_found = go_hor(matrix, pos, step)
            ver = True

    return matrix


matrix = []
for line in lines:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    matrix.append(row)

matrix = walk(matrix)
count = 0
for row in matrix:
    count += row.count('X')

print(count)
