words = []
with open('lines.txt') as file:
    for line in file:
        for s in line.strip('\n').split():
            if s.isalpha():
                words.append(s)
print(max(words, key=len))
