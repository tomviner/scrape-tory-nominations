# Tory nomination scraper

A [git scraper](https://simonwillison.net/2020/Oct/9/git-scraping/) that records various spreadsheets containing listings of declared Conservative nominations for leadership candidates, so changes are visible.

- Guido Fawkes [Tory Leadership: Who's Backing Who October Election](https://docs.google.com/spreadsheets/d/1PRufWhh2YAoxPUJEXeVaEOe7rcT1IINOXijeLI6o9Cc/htmlview)
    ![image](https://github.com/tomviner/scrape-tory-nominations/blob/main/gf-noms-time-series.png?raw=true))

- [Smarkets Conservative leadership election tracker (October 2022)](https://docs.google.com/spreadsheets/d/1t1MaeGTmOvmOOkUL8TDDJwqTTc-N1wmRxPeRe0k3yjM/htmlview)

Attempts exports as CSV every 5 minutes, although Github actions seems to run less often than this.

Inspired by [Simon Willison](https://twitter.com/simonw/)'s [Half Moon Bay Pumpkin Festival scraper](https://github.com/simonw/scrape-hmb-traffic).

## Workflow
- download spreadsheet as csv
- convert to sqlite db with git-history
- query db using sqlite-utils to export time series
- generate graph
