import argparse

parser = argparse.ArgumentParser(
    description='Print arg'
)
parser.add_argument('arg')
args = parser.parse_args()
print(args.arg)
