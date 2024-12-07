with open('./input.txt', 'r') as f:
    lines = f.readlines()


def to_base3(num):
    if num == 0:
        return "0"
    base3 = []
    while num > 0:
        base3.append(str(num % 3))
        num //= 3
    return ''.join(reversed(base3))


def convert_inverse(string):
    if string == '0':
        return '+'
    elif string == '1':
        return '*'
    elif string == '2':
        return '|'


def convert(string):
    if string == '+':
        return '0'
    elif string == '*':
        return '1'
    elif string == '|':
        return '2'


def next(spots):
    if '+' not in spots and '*' not in spots:
        return None
    base3 = map(convert, spots)
    num = int(''.join(list(base3)), 3) + 1
    base3 = str(to_base3(num))
    if len(base3) < len(spots):
        base3 = '0'*(len(spots) - len(base3)) + base3
    spots = map(convert_inverse, base3)
    return list(spots)


def find_operators(equation):
    result = equation[0]
    numbers = equation[1:]
    spots = ['+']*(len(numbers) - 1)
    while True:
        sub_result = 0
        for i, operator in enumerate(spots):
            if operator == '|':
                if i == 0:
                    sub_result = int(str(numbers[i]) + str(numbers[i + 1]))
                else:
                    sub_result = int(str(sub_result) + str(numbers[i + 1]))
            elif operator == '+':
                if i == 0:
                    sub_result = numbers[0] + numbers[1]
                else:
                    sub_result = sub_result + numbers[i + 1]
            else:
                if i == 0:
                    sub_result = numbers[0] * numbers[1]
                else:
                    sub_result = sub_result * numbers[i + 1]
        if sub_result == result:
            break
        else:
            spots = next(spots)
            if spots is None:
                return 0

    return result


equations = []
for line in lines:
    line = line.strip()
    parts = line.split(': ')
    result = int(parts[0])
    equation = [int(x) for x in parts[1].split()]
    equations.append([result] + equation)

total = 0
for i, equation in enumerate(equations):
    total += find_operators(equation)

print(total)
