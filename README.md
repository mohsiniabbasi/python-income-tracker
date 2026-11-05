# UK Self-Employed Workers' Income Tracker

Record your daily income and expenses, see how much you have earned every week, and get an estimate of the tax you owe so far.

Built for UK self-employed workers (taxi and private-hire drivers, couriers, trades) who get paid daily and want to know where they stand before the Self Assessment deadline, not after it.

There are two ways to use it:

- **Menu mode** (`tracker.py`): a numbered menu, standard library only.
- **Assistant mode** (`agent.py`): ask in plain English, e.g. *"I made 280 today and spent 25 on fuel"* or *"what did I earn last Tuesday?"*

## Features

- Add your income and expenses for the day; more than one entry per day is allowed (e.g. a morning and an evening shift)
- **Missing-days catch-up**: when the assistant starts, it asks for every day since your first entry that has no record (`0 0` = didn't work)
- See the totals for any week of the tax year, or any day by date (`yyyy-mm-dd`)
- List every week and every month with income, expenses and profit
- **Yearly costs** (insurance, MOT, road tax, council licence): add, list and delete them; they come off your profit for that tax year
- Running totals for the current tax year, shown every time the menu opens
- **Estimated tax so far**, including the higher rate above £50,270
- Safe input: letters, empty replies or one number instead of two ask again instead of crashing
- Entries are saved to local files, so nothing is lost when you close the program

## How the assistant works

The assistant is a **grounded tool-calling agent**, not a chatbot:

1. Gemini reads your question and picks **one tool**: add an entry, a day, a week, or the totals.
2. **Python** works out the numbers from your own saved entries. The AI never does the maths.
3. You get a one-line answer built only from that data.

Guardrails:

- It refuses anything that isn't about your records ("I can only answer about your income records")
- Negative amounts are turned positive
- Nothing is saved until you confirm with `yes`
- If the AI's reply doesn't match a tool, it asks you again

## How it works

- **Weeks follow the UK tax year** (6 April – 5 April). Week 1 starts on 6 April, and the tax year is worked out automatically from the date.
- **April is split in two**: 1–5 April belongs to the previous tax year and 6–30 April to the new one, so the monthly list shows `2027-04 (1-5)` and `2027-04 (6-30)`.
- **Each entry stores its tax year**, so week 28 of one year is never mixed with week 28 of the next.
- **Tax estimate (2026–27, England)**: the Personal Allowance (£12,570) and the basic-rate band (£37,700) are spread across the weeks so far. Profit in the basic band is charged at 26% (20% Income Tax + 6% Class 4 NI). Profit above the band is charged at 42% (40% + 2%).

## How to run

Requires Python 3.

**Menu mode** (nothing to install):

```
python tracker.py
```

```
1--- Add today's income and expenses
2--- Which week number you want to see
3--- Enter a date (yyyy-mm-dd) to see that day's figures
4--- Show all weeks
5--- Show all months
6--- Add a yearly cost
7--- Show yearly costs
8--- Delete a yearly cost
x--- Exit
```

**Assistant mode** needs a free Gemini API key:

```
python -m pip install requests python-dotenv
```

Create a file called `.env` next to `agent.py` containing:

```
GEMINI_API_KEY=your-key-here
```

Then run:

```
python agent.py
```

## Run the tests

8 tests with `pytest`. Each one runs a function on fixed data and checks it against an answer worked out by hand:

- **Months**: the April split, including the edge days 5 and 6 April
- **Weeks**: 6 April is week 1 of the new tax year; 5 April is week 53 of the old one
- **Missing days**: a fake diary with a gap returns exactly the missing dates
- **Tax**: full-year profit of £30,000, £50,270 (the exact edge of the higher-rate band) and £60,000

```
python -m pip install pytest
python -m pytest
```

## Privacy

Your figures are saved in `entries.json` and `entries-costs.json` on your own computer only. Both files and your `.env` key are listed in `.gitignore`, so they are never uploaded to GitHub. In assistant mode, only your question and today's date are sent to Gemini. Your saved figures are not, because Python writes the answer.

## Limitations

The tax figure is an **estimate, not a tax return**. It does not include the 45% additional rate, the Personal Allowance taper above £100,000, or Scottish rates. Yearly costs come off in full while the allowance is spread across the weeks, so the estimate is low early in the tax year.

## Roadmap

- First run of a tax year: ask for yearly costs, then reuse last year's names next year
- Let the assistant add and list yearly costs
- Version 3: SQLite database instead of JSON files
- Version 4: a simple web dashboard with a clickable list of weeks

## What I learned

Functions with parameters and return values, `while` loops and menus, `if/elif/else`, input validation with `try/except`, lists and dictionaries, dates with `datetime` and `timedelta`, saving and loading JSON, calling an AI API with `requests`, keeping secrets in `.env`, testing with `pytest`, and using Git and GitHub from the command line.

## Author

Mohsan Abasi, Pivot Bureau (Dewsbury, UK)
