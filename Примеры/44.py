import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d',
    '--debug',
    action='store_true'
)
args = parser.parse_args()
print(args.debug)
