from sys import stdin


d = {}
for line in stdin:
    line = line.rstrip('\n').split()
    d.update({word[0]: d.get(word[0], []) + [word] for word in line})

for key in sorted(d.keys()):
    print(f'{key}: {" ".join(sorted(d[key]))}')