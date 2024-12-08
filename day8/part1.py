with open('./input.txt', 'r') as f:
    lines = f.readlines()


def find_locations(matrix):
    locs = {}
    for row in matrix:
        for char in row:
            if char != '.' and char not in locs:
                locs[char] = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != '.':
                locs[matrix[i][j]].append((i, j))

    return locs


def check_point(c1, locs):
    for key in locs.keys():
        distances = [(loc[0] - c1[0], loc[1] - c1[1]) for loc in locs[key]]
        for dist in distances:
            if dist == (0, 0):
                continue
            if (dist[0]*2, dist[1]*2) in distances:
                return 1

    return 0


matrix = []
for line in lines:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    matrix.append(row)


total = 0
locs = find_locations(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        total += check_point((i, j), locs)

print(total)
