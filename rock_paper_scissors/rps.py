#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    cache = [None for i in range(n+1)]

    def permute(n):
        pass

    return permute(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
