from sys import stdin

total = 0
for line in stdin:
    for number in line.split():
        total += int(number)

print(total)
