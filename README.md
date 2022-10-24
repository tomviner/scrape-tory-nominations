# Tory nomination scraper

A [git scraper](https://simonwillison.net/2020/Oct/9/git-scraping/) that records various spreadsheets containing listings of declared Conservative nominations for leadership candidates, so changes are visible.

![image](https://github.com/tomviner/scrape-tory-nominations/blob/main/joint-time-series.png?raw=true)

## Data sources:
- Guido Fawkes [Tory Leadership: Who's Backing Who October Election](https://docs.google.com/spreadsheets/d/1PRufWhh2YAoxPUJEXeVaEOe7rcT1IINOXijeLI6o9Cc/htmlview)

Latest:
<!-- [[[cog
import cog
from headline_numbers import make_table
table = make_table('gf-noms-time-series.csv')
cog.out(table)
]]] -->
|                 |   Rishi Sunak | Boris Johnson   |   Penny Mordaunt |
|---------------------|---------------|-----------------|------------------|
| 2022-10-24 12:52:01 |           202 |                 |               30 |
<!-- [[[end]]] -->

![image](https://github.com/tomviner/scrape-tory-nominations/blob/main/gf-noms-time-series.png?raw=true)


- [Smarkets Conservative leadership election tracker (October 2022)](https://docs.google.com/spreadsheets/d/1t1MaeGTmOvmOOkUL8TDDJwqTTc-N1wmRxPeRe0k3yjM/htmlview)

Latest: <!-- [[[cog
import cog
from headline_numbers import make_table
table = make_table('smarkets-leaderboard-time-series.csv')
cog.out(table)
]]] -->
|                 |   Rishi Sunak |   Boris Johnson |   Penny Mordaunt |
|---------------------|---------------|-----------------|------------------|
| 2022-10-24 11:50:47 |           185 |              47 |               29 |
<!-- [[[end]]] -->

![image](https://github.com/tomviner/scrape-tory-nominations/raw/main/smarkets-leaderboard-time-series.png?raw=true)


## Workflow
- download spreadsheet as csv
- convert to sqlite db with [git-history](https://pypi.org/project/git-history/) (see this repos requirement.txt to include https://github.com/simonw/git-history/pull/59)
- query db using [sqlite-utils](https://pypi.org/project/sqlite-utils/) to export time series
- generate graph

Attempts exports as CSV every 5 minutes, although Github actions seems to run less often than this.

Inspired by [Simon Willison](https://twitter.com/simonw/)'s [Half Moon Bay Pumpkin Festival scraper](https://github.com/simonw/scrape-hmb-traffic).
