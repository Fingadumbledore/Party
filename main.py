""" used for argument parsing and starting the server """
import argparse
from server import server

def main():
    """ entrypoint to program """
    parser = argparse.ArgumentParser(
                        prog = 'Party Controller',
                        description = 'Manage Lan parties',
                        epilog = 'thanks for using')

    parser.add_argument('-s', '--start', action='store_true', help="startet Server")
    parser.add_argument('-l', '--load', action='store_true', help="lädt alte Session")
    parser.add_argument('-o', '--output', action='store_true', help="setzt output Pfad")

    args = parser.parse_args()

    if args.start:
        server()

    elif args.load:
        server()

    elif args.output:
        print("schön für dich")

    else:
        parser.print_help()

if __name__ == "__main__":
    exit(main())
