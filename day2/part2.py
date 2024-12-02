with open('./input.txt', 'r') as f:
    lines = f.readlines()

safe_count = 0
for i, line in enumerate(lines):
    parts = [int(part) for part in line.strip().split(' ')]
    safe = False
    for k in range(len(parts)):
        sub_safe = True
        parts_strip = parts[:k] + parts[k + 1:]
        asc = parts_strip[1] > parts_strip[0]
        for j in range(1, len(parts_strip)):
            if parts_strip[j - 1] == parts_strip[j]:
                sub_safe = False
                break
            if asc:
                if parts_strip[j - 1] > parts_strip[j] or abs(parts_strip[j - 1] - parts_strip[j]) > 3:
                    sub_safe = False
                    break
            else:
                if parts_strip[j - 1] < parts_strip[j] or abs(parts_strip[j - 1] - parts_strip[j]) > 3:
                    sub_safe = False
                    break
        if sub_safe:
            safe = True
            break
    safe_count = safe_count + 1 if safe else safe_count

print(safe_count)
