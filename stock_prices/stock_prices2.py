#!/usr/bin/python

import argparse


def find_max_profit(prices):
    highest_profit = -float('inf')

    for i, buy_price in enumerate(prices):
        subsequent_prices = prices[i+1:]

        if subsequent_prices:
            max_price = max(subsequent_prices)
            profit = max_price - buy_price

            if profit > highest_profit:
                highest_profit = profit

    return highest_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
