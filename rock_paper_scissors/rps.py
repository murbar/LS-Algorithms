#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    permutations = []
    # cache = [None for i in range(n+1)]

    def permute(round, round_number):
        for play in plays:
            round.append(play)
            if round_number == n:
                permutations.append([*round])
            else:
                permute(round, round_number + 1)
            round.pop()

    permute([], 1)

    return permutations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
