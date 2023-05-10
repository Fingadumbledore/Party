""" used for argument parsing and starting the server """
import argparse
from server import server
from database import mate_erstellen

def main():
    """ entrypoint to program """
    parser = argparse.ArgumentParser(
                        prog = 'Party Controller',
                        description = 'Manage LAN Parties',
                        epilog = 'thanks for using')

    parser.add_argument('-s', '--start', action='store_true', help="startet Server")
    parser.add_argument('-l', '--load', action='store_true', help="lädt alte Session")
    parser.add_argument('-o', '--output', action='store_true', help="setzt output Pfad")

    args = parser.parse_args()

    if args.start:
        mate_erstellen()
        server()

    elif args.load:
        server()

    elif args.output:
        print("schön für dich")

    else:
        parser.print_help()

if __name__ == "__main__":
    exit(main())
