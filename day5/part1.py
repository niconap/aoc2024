with open('./input.txt', 'r') as f:
    lines = f.readlines()


def validate_update(rules, update):
    updated = []
    valid = True
    for i in range(len(update)):
        relevant = [rule for rule in rules if rule[1] == update[i]]
        for rule in relevant:
            if rule[0] not in updated and rule[0] in update[i:]:
                valid = False
                return 0
        updated.append(update[i])
    if valid:
        return update[int((len(update) - 1)/2)]


switch = False
rules = []
updates = []
for line in lines:
    if line == '\n':
        switch = True
        continue
    if not switch:
        line = line.strip()
        parts = line.split('|')
        rules.append((int(parts[0]), int(parts[1])))
    else:
        line = line.strip()
        parts = line.split(',')
        updates.append([int(part) for part in parts])

total = 0
for update in updates:
    total += validate_update(rules, update)
print(total)
