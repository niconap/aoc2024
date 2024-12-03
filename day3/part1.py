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
        muls.append((int(digit1), int(digit2)))
        part = part[i:]


with open('./input.txt', 'r') as f:
    lines = f.readlines()

result = 0
for line in lines:
    for mul in extract_muls(line):
        result += mul[0]*mul[1]

print(result)
