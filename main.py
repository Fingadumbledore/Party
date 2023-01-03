import argparse

parser = argparse.ArgumentParser(
                    prog = 'Party Controller',
                    description = 'Manage Lan parties',
                    epilog = 'thanks for using')

parser.add_argument('filename')           # positional argument
parser.add_argument('-s', '--start')      # option that takes a value
parser.add_argument('-l', '--load')

args = parser.parse_args()
print(args.filename, args.start, args.load)