#!/usr/bin/python

import sys

# think of it as permutations of words with length n containing possible letters 'r', 'p', & 's'


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    permutations = []
    cache = [None for i in range(n+1)]

    def play(rounds, accumulator=[]):
        if rounds == 0:
            permutations.append([*accumulator])
            return

        for p in plays:
            play(rounds - 1, accumulator + [p])

    play(n)

    return permutations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
