f = open('text.txt', mode='r', encoding='utf8')
lines = []
for line in f:
    lines.append(line)
print(lines)
f.close()
