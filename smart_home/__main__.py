#!/usr/bin/env python

"""Smart Home main"""

import argparse

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description='Smart Home tasks launcher.')

    PARSER.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')

    PARSER.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    ARGS = PARSER.parse_args()
    print(ARGS.accumulate(ARGS.integers))
