import argparse

parser = argparse.ArgumentParser(
    description='Print sum or avg of the number'
)
parser.add_argument('numbers', nargs='+', type=int)
parser.add_argument(
    '--avg',
    action='store_true',
    help='Print avg, default sum'
)
args = parser.parse_args()
total = sum(args.numbers)
if args.avg:
    print(total / len(args.numbers))
else:
    print(total)
