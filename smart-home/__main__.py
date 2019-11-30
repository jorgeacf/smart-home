#!/usr/bin/env python

"""Smart Home main"""

import nmap
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Smart Home tasks launcher.')

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')

    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
