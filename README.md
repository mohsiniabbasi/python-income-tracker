# UK Self-Employed Workers' Income Tracker

Record your daily income and expenses, and see how much you have earned every week. Once your profit is above the tax-free Personal Allowance (£12,570), it also shows an estimate of the tax you owe so far.

Built for UK self-employed workers (taxi and private-hire drivers, couriers, trades) who get paid daily and want to know where they stand before the Self Assessment deadline, not after it.

## Features

- Add your income and expenses for today; more than one entry per day is allowed (e.g. a morning and an evening shift)
- See the totals for any week of the tax year
- Look up any day by date (`yyyy-mm-dd`)
- List every week and every month with income, expenses and profit
- Running totals for the current tax year, shown every time the menu opens
- Estimated tax so far, based on profit above the Personal Allowance
- Safe input: typing letters instead of a number asks again instead of crashing
- Entries are saved to a local file, so nothing is lost when you close the program

## How it works

- **Weeks follow the UK tax year** (6 April – 5 April). Week 1 starts on 6 April; the tax year is worked out automatically from today's date.
- **April is split in two**: 1–5 April belongs to the previous tax year, 6–30 April to the new one, so the monthly list shows `2027-04 (1-5)` and `2027-04 (6-30)`.
- **Each entry stores its tax year**, so week 28 of one year is never mixed with week 28 of the next, and the totals and tax estimate only count the current tax year.
- **Tax estimate**: the Personal Allowance is spread across the 52 weeks so far; profit above that is charged at 20% Income Tax + 6% Class 4 National Insurance (2026–27 basic-rate figures).

## How to run

Requires Python 3 (standard library only, nothing to install).

```
python tracker.py
```

Then choose from the menu:

```
1--- Add today's income and expenses
2--- Which week number you want to see
3--- Enter a date (yyyy-mm-dd) to see that day's figures
4--- Show all weeks
5--- Show all months
x--- Exit
```

Example:

```
Total so far: Income £150.00, Total Expenses: £25.00, Total Profit: £125.00 , Tax so far (est): £0.00
Week number 28 Income: £150.00, Expenses: £25.00, Profit: £125.00
Month 2026-04 (1-5) Income: £200.00, Expenses: £40.00, Profit: £160.00
Month 2026-04 (6-30) Income: £320.00, Expenses: £65.00, Profit: £255.00
```

## Run the tests

The tests check the tax-year month split (1–5 April, 6–30 April and normal months), including the edge days 5 and 6 April.

```
python -m pip install pytest
python -m pytest
```

## Privacy

Your figures are saved in `entries.json` on your own computer only. The file is listed in `.gitignore`, so it is never uploaded to GitHub.

## Limitations

The tax figure is an **estimate, not a tax return**. It uses the basic rate only (no higher rate above £50,270), does not yet include yearly costs such as insurance, MOT, road tax or licence fees, and is based on England, Wales and Northern Ireland rates.

## Roadmap

- Yearly one-off expenses (insurance, MOT, council licence, road tax) that can be added or deleted
- Higher-rate tax bands
- Version 2: SQLite database instead of a JSON file
- Version 3: monthly reports and CSV export with pandas
- Version 4: a simple web dashboard with a clickable list of weeks
- Version 5: a REST API with FastAPI

## What I learned

Functions with parameters and return values, `while` loops and menus, `if/elif/else`, input validation with `try/except`, lists and dictionaries, string slicing, dates with `datetime`, saving and loading JSON, and using Git and GitHub from the command line.

## Author

Mohsan Abasi, Pivot Bureau (Dewsbury, UK)
