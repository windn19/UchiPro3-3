with open('numbers.txt') as file:
    total = 0
    for line in file:
        for number in line.split():
            total += int(number)

    print(total)
