import sys

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

in_file, out_file = sys.argv[1:]

df = pd.read_csv(in_file)
df.date =  pd.to_datetime(df.date)

plt.gca().xaxis.set_major_formatter(DateFormatter("%d %H:%M"))
plt.xticks(rotation=45, fontsize='small')
candidates = df.drop('date', axis=1)

for column in candidates.columns:
    plt.plot(df.date, df[column])
plt.legend(candidates)

plt.savefig(out_file)
