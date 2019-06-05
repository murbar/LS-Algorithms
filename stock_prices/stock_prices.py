#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profits = []
    for i in range(len(prices) - 1):
        price = prices[i]
        subsequent_prices = prices[i+1:]
        highest_price = max(subsequent_prices)
        profits.append(highest_price - price)
        # for s in subsequent_prices:
        #     profit = s - p
        #     if profit > max_profit:
        #         max_profit = profit
    return max(profits)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
