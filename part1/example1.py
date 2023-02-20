from sys import stdin


total = 0
for line in stdin:
    line = line.rstrip('\n')
    if line.isdigit():
        total += int(line)

print(total)
