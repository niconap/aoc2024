# I am so sorry for creating this abomination
with open('./input.txt', 'r') as f:
    lines = f.readlines()


def go_hor(matrix, pos, step, total_seen):
    end_found = False
    loop_found = False
    while pos[1] + step >= 0 and pos[1] + step < len(matrix[0]):
        if (pos[0], pos[1], 0, step) in total_seen:
            loop_found = True
            return matrix, pos, end_found, loop_found
        if matrix[pos[0]][pos[1] + step] == '#':
            total_seen.update([(pos[0], pos[1], 0, step)])
            break
        total_seen.update([(pos[0], pos[1], 0, step)])
        pos[1] += step
    if pos[1] + step < 0 or pos[1] + step >= len(matrix[0]):
        total_seen.update([(pos[0], pos[1], 0, step)])
        end_found = True
    return matrix, pos, end_found, loop_found


def go_ver(matrix, pos, step, total_seen):
    end_found = False
    loop_found = False
    while pos[0] + step >= 0 and pos[0] + step < len(matrix):
        if (pos[0], pos[1], step, 0) in total_seen:
            loop_found = True
            return matrix, pos, end_found, loop_found
        if matrix[pos[0] + step][pos[1]] == '#':
            total_seen.update([(pos[0], pos[1], step, 0)])
            break
        total_seen.update([(pos[0], pos[1], step, 0)])
        pos[0] += step
    if pos[0] + step < 0 or pos[0] + step >= len(matrix):
        total_seen.update([(pos[0], pos[1], step, 0)])
        end_found = True
    return matrix, pos, end_found, loop_found


def walk(matrix):
    total_seen = set()
    total_pos = 0
    pos = None
    original_pos = None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '^':
                pos = [i, j]
                original_pos = (i, j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '.':
                continue
            matrix[i][j] = '#'
            ver = True
            step = -1
            end_found = False
            loop_found = False
            while not end_found and not loop_found:
                if ver:
                    matrix, pos, end_found, loop_found = go_ver(
                        matrix, pos, step, total_seen)
                    ver = False
                    step *= -1
                elif not ver:
                    matrix, pos, end_found, loop_found = go_hor(
                        matrix, pos, step, total_seen)
                    ver = True
            if loop_found:
                total_pos += 1
            total_seen = set()
            matrix[i][j] = '.'
            pos = [original_pos[0], original_pos[1]]

    return total_pos


matrix = []
for line in lines:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    matrix.append(row)

total = walk(matrix)
print(total)
