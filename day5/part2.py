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
                return valid
        updated.append(update[i])
    return valid


def correct_update(rules, update):
    relevant = [rule for rule in rules if rule[0]
                in update and rule[1] in update]
    corrected = []

    for page in update:
        seconds = [rule for rule in relevant if rule[1] == page]
        if len(seconds) == 0:
            corrected.append(page)
            update.remove(page)
            break

    while True:
        for page in update:
            seconds = [rule for rule in relevant if rule[1]
                       == page and rule[0] not in corrected]
            if len(seconds) == 0:
                corrected.append(page)
                update.remove(page)
                break
        if len(update) == 0:
            break

    return corrected[int((len(corrected) - 1)/2)]


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

incorrect = []
for update in updates:
    if not validate_update(rules, update):
        incorrect.append(update)

total = 0
for update in incorrect:
    total += correct_update(rules, update)

print(total)
