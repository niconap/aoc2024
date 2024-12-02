with open('./input.txt', 'r') as f:
    lines = f.readlines()

safe_count = 0
for i, line in enumerate(lines):
    parts = [int(part) for part in line.strip().split(' ')]
    safe = True
    asc = parts[1] > parts[0]
    for j in range(1, len(parts)):
        if parts[j - 1] == parts[j]:
            safe = False
            break
        if asc:
            if parts[j - 1] > parts[j] or abs(parts[j - 1] - parts[j]) > 3:
                safe = False
                break
        else:
            if parts[j - 1] < parts[j] or abs(parts[j - 1] - parts[j]) > 3:
                safe = False
                break
    safe_count = safe_count + 1 if safe else safe_count

print(safe_count)
