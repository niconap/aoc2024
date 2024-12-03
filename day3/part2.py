def extract_muls(line):
    muls = []
    part = line
    while part[0] != '\n':
        if len(part) < 8:
            return muls
        mul_pos = part.find('mul(')
        if mul_pos == -1:
            return muls
        part = part[mul_pos:]
        abs_mul_pos = line.find(part)

        digit1 = ''
        i = 4
        while part[i].isdigit():
            digit1 += part[i]
            i += 1
        if part[i] != ',':
            part = part[i:]
            continue

        digit2 = ''
        i += 1
        while part[i].isdigit():
            digit2 += part[i]
            i += 1
        if part[i] != ')':
            part = part[i:]
            continue
        muls.append((int(digit1), int(digit2), abs_mul_pos))
        part = part[i:]


def extract_dos(line):
    positions = []
    start = 0
    while True:
        pos = line.find('do()', start)
        if pos > 0:
            positions.append(pos)
        else:
            break
        start = pos + 1
    return positions


def extract_donts(line):
    positions = []
    start = 0
    while True:
        pos = line.find('don\'t()', start)
        if pos > 0:
            positions.append(pos)
        else:
            break
        start = pos + 1
    return positions


with open('./input.txt', 'r') as f:
    lines = f.readlines()

result = 0
prev_disabled = False
for line in lines:
    dos = extract_dos(line)
    donts = extract_donts(line)
    if prev_disabled:
        donts.insert(0, -1)
        dos.insert(0, -2)
    else:
        dos.insert(0, -1)
        donts.insert(0, -2)
    for mul in extract_muls(line):
        last_dont = max([n for n in donts if n < mul[2]])
        last_do = max([y for y in dos if y < mul[2]])
        if last_do > last_dont:
            result += mul[0]*mul[1]

    if donts[-1] > dos[-1]:
        prev_disabled = True
    else:
        prev_disabled = False

print(result)
