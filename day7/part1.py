with open('./input.txt', 'r') as f:
    lines = f.readlines()


def next(spots):
    if '+' not in spots:
        return None
    binary = map(lambda x: '1' if x == '*' else '0', spots)
    num = int(''.join(list(binary)), 2) + 1
    binary = bin(num)[2:]
    if len(binary) < len(spots):
        binary = '0'*(len(spots) - len(binary)) + binary
    spots = map(lambda x: '*' if x == '1' else '+', binary)
    return list(spots)


def find_operators(equation):
    result = equation[0]
    numbers = equation[1:]
    spots = ['+']*(len(numbers) - 1)
    while True:
        sub_result = 0
        for i, operator in enumerate(spots):
            if operator == '+':
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
for equation in equations:
    total += find_operators(equation)

print(total)
