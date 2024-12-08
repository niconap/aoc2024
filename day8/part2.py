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


def beam(locs, max_x, max_y):
    antinodes = set()
    for i in range(len(locs)):
        curr = locs[i]
        for loc in locs[i + 1:]:
            xdiff = loc[0] - curr[0]
            ydiff = loc[1] - curr[1]
            spot = [curr[0], curr[1]]
            while spot[0] - xdiff >= 0 and spot[0] - xdiff < max_x and \
                    spot[1] - ydiff >= 0 and spot[1] - ydiff < max_y:
                spot = [spot[0] - xdiff, spot[1] - ydiff]
            while spot[0] < max_x and spot[0] >= 0 and \
                    spot[1] < max_y and spot[1] >= 0:
                antinodes.add((spot[0], spot[1]))
                spot = [spot[0] + xdiff, spot[1] + ydiff]

    return antinodes


matrix = []
for line in lines:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    matrix.append(row)


total = 0
locs = find_locations(matrix)
spots = set()
for key in locs.keys():
    antinodes = beam(locs[key], len(matrix), len(matrix[0]))
    spots.update(antinodes)

print(len(spots))
