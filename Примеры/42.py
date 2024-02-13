import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'values',
    nargs='*',
    default=[1, 2, 3],
    type=int)
args = parser.parse_args()
print(args.values)
