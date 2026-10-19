from datetime import datetime, date
import json

PERSONAL_ALLOWANCE = 12570
BASIC_RATE = 0.20
NI_RATE = 0.06

def ask_amount(question):

    while True:
        try:
            amount = float(input(question))
            return amount
        except ValueError:
            print("Invalid input. Please numbers only.")

def show_week(week_number):
    week_income = 0
    week_expenses = 0
    for e in entries:
        if e["week"] == week_number and e["tax_year"] == tax_year:
            week_income = week_income + e["income"]
            week_expenses = week_expenses + e["expenses"]
    week_profit = week_income - week_expenses
    print(f"Week number {week_number} Income: £{week_income:.2f}, Expenses: £{week_expenses:.2f}, Profit: £{week_profit:.2f}")

def show_total():
    total_income = 0
    total_expenses = 0
    for e in entries:
        if e["tax_year"] == tax_year:
            total_income = total_income + e["income"]
            total_expenses = total_expenses + e["expenses"]
    total_profit = total_income - total_expenses
    allowance_so_far = PERSONAL_ALLOWANCE * week / 52
    taxable = total_profit - allowance_so_far
    if taxable < 0:
        taxable = 0
    tax_estimate = taxable * (BASIC_RATE + NI_RATE)
    print(f"Total so far: Income £{total_income:.2f}, Total Expenses: £{total_expenses:.2f}, Total Profit: £{total_profit:.2f} , Tax so far (est): £{tax_estimate:.2f}")

def show_day(chosen_date):
    day_income = 0
    day_expenses = 0
    for e in entries:
        if e["date"] == chosen_date:
            day_income = day_income + e["income"]
            day_expenses = day_expenses + e["expenses"]
    day_profit = day_income - day_expenses
    print(f"Day {chosen_date} Income: £{day_income:.2f}, Expenses: £{day_expenses:.2f}, Profit: £{day_profit:.2f}")

def show_all_weeks():
    weeks= []
    for e in entries:
        if e["week"] not in weeks:
            weeks.append(e["week"])
    weeks.sort()
    for w in weeks:
        show_week(w)

def month_label(date_text):
    month = date_text[:7]
    if date_text[5:7] == "04":
        day = int(date_text[8:10])
        if day < 6:
            month = month + " (1-5)"
        else:            
            month = month + " (6-30)"
    return month

def show_all_months():
    months= []
    for e in entries:
        if month_label(e["date"]) not in months:
            months.append(month_label(e["date"]))
    months.sort()
    for m in months:
        show_month(m)

def show_month(month):
    month_income = 0
    month_expenses = 0
    for e in entries:
        if month_label(e["date"]) == month:
            month_income = month_income + e["income"]
            month_expenses = month_expenses + e["expenses"]
    month_profit = month_income - month_expenses
    print(f"Month {month} Income: £{month_income:.2f}, Expenses: £{month_expenses:.2f}, Profit: £{month_profit:.2f}")

today = datetime.now().date()
#tax_year_start = date(2026, 4, 6)
if today >= date(today.year, 4, 6):
    tax_year_start = date(today.year, 4, 6)
else:
    tax_year_start = date(today.year - 1, 4, 6)
days = (today - tax_year_start).days
week = days // 7 + 1
tax_year = tax_year_start.year

try:

    f = open("entries.json", "r")
    entries = json.load(f)
    f.close()
except FileNotFoundError:
    entries = []

while True:
    show_total()
    print("1--- Add today's income and expenses: ")
    print("2--- Which week number you want to see: ")
    print("3--- Enter a date (yyyy-mm-dd) to see that day's figures: ")
    print("4--- Show all weeks: ")
    print("5--- Show all months: ")
    print("x--- Exit: ")
    choice = input("Choose: ")
    if choice == "1":
        daily_income = ask_amount("Enter your today's income: £")
        daily_expenses = ask_amount("Enter your today's expenses: £")

        daily_profit = daily_income - daily_expenses
        print(f"Date: {today}, Week: {week}, Daily Profit: £{daily_profit:.2f}")

        entry = {"date": str(today), "week": week, "tax_year": tax_year, "income": daily_income, "expenses": daily_expenses, "profit": daily_profit}
        print("Daily Profit Entry:", entry)

        entries.append(entry)

        f = open("entries.json", "w")
        json.dump(entries, f, indent=2)
        f.close()
        print("Entries saved to entries.json")
        print("This week so far: ")
        show_week(week)

    elif choice == "2":
       choose = int(ask_amount("Enter the week number : "))
       show_week(choose)
    elif choice == "3":
        chosen_date = input("Enter a date (yyyy-mm-dd): ")
        show_day(chosen_date)
    elif choice == "4":
        show_all_weeks()
    elif choice == "5":
        show_all_months()
    elif choice == "x":
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, 5, x.")