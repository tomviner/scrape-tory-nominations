import csv
import sys

from tabulate import tabulate


def make_table(infile):
    rows = csv.DictReader(open(infile))

    head = next(rows)

    return tabulate([head], headers="keys", tablefmt="github").replace('date', '')


if __name__ == '__main__':
    infile = sys.argv[1]
    table = make_table(infile)
    print(table)
