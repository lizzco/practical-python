# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    '''
    Calculate the total cost of the portfolio
    '''
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(f)
        for row in rows:
            try:
                total_cost = total_cost + (float(row[2]) * int(row[1]))
            except ValueError:
                print("Couldn't parse", row)
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)
