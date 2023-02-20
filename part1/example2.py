with open('text_num.txt', encoding='utf8') as f:
    lines = f.readlines()

total = 0
for line in lines:
    line = line.rstrip('\n')
    if line.isdigit():
        total += int(line)

print(total)
