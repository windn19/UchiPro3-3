from sys import stdin

d = {}
for line in stdin:
    for w in line.split():
        if w[0] not in d:
            d[w[0]] = [w]
        else:
            d[w[0]].append(w)

for key in sorted(d):
    print(f'{key}: {" ".join(sorted(d[key]))}')
