import random
import sys

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import TABLEAU_COLORS
from matplotlib.dates import DateFormatter

*in_files, out_file = sys.argv[1:]


def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return "#%02x%02x%02x" % (red, green, blue)


def get_index(item, items):
    try:
        return items.index(item)
    except ValueError:
        items.append(item)
        return len(items) - 1


def get_colour(major, minor, majors=[], minors=[]):
    colours = [
        # 3 candidates high, by 2 sheet compilers wide
        ["tab:blue", "tab:cyan"],
        ["tab:orange", "#fcc28e"],
        ["tab:green", "tab:olive"],
    ]
    major_idx = get_index(major, majors)
    minor_idx = get_index(minor, minors)
    name = colours[major_idx][minor_idx]
    return TABLEAU_COLORS.get(name, name)


plt.gca().xaxis.set_major_formatter(DateFormatter("%d %H:%M"))
plt.xticks(rotation=45, fontsize="small")

for in_file in in_files:
    df = pd.read_csv(in_file)
    df.date = pd.to_datetime(df.date)

    candidates = df.drop("date", axis=1)

    for column in candidates.columns:
        color = get_colour(column, in_file)
        label = f"{in_file[:3]}-{column}"
        plt.plot(df.date, df[column], color=color, label=label)
    plt.legend(candidates)

    # special case for multi-dataset
    if len(in_files) > 1:
        plt.title("Totals for Guido Fawkes (legend), and Smarkets (lighter shades)")


plt.savefig(out_file)
