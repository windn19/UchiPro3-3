import argparse

types = ['all', 'odd', 'even']

parser = argparse.ArgumentParser()
parser.add_argument('-count', type=int, default=100)
parser.add_argument('-start', type=int, default=1)
parser.add_argument('-type', choices=types, default='all')

args = parser.parse_args()


def get_numbers(start, count, type):
    n = start
    result = []
    while len(result) < count:
        if type == 'odd':
            if n % 2 != 0:
                result.append(n)
        elif type == 'even':
            if n % 2 == 0:
                result.append(n)
        elif type == 'all':
            result.append(n)
        n += 1
    return result


result = get_numbers(args.start, args.count, args.type)
print(*result, sep=', ')
