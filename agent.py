import requests
from dotenv import load_dotenv
import os
from tracker import week_figures, day_figures, total_figures, add_entry, today, week, tax_year, missing_dates

load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

def ask_gemini(question):
    url1 = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"
    headers = {"x-goog-api-key": gemini_key}
    body = {"contents": [{"parts": [{"text" : question}]}]}
    response = requests.post(url1, headers=headers, json=body)
    data = response.json()
    answer = data["candidates"][0]["content"]["parts"][0]["text"]
    return answer

print("Hi, I’m your income tracker assistant.")
print("Add today’s income and expenses, or see a day, a week, or your totals and tax so far \n For example: I made 280 today and spent 25 on fuel")

for missing_day in missing_dates():
    reply = input(f"No entry for {missing_day}. Type income and expenses like 102 12, or 0 0 if you did not work: ")
    numbers = reply.split()
    day_income = abs(float(numbers[0]))
    day_expenses = abs(float(numbers[1]))
    add_entry(missing_day, day_income, day_expenses)

while True:
    question = input("\nWhat would you like to do? (x to exit): ")
    if question == "x":
        break

    choose = ("Today is " + today.strftime("%A %Y-%m-%d") + ". This is week " + str(week) + " of the tax year. "
              "Pick the tool for the question. Tools: "
              "week N (figures for tax-year week N), "
              "day YYYY-MM-DD (figures for one date), "
              "total (totals and tax estimate for this tax year), "
              "add followed by today's income and expenses as two numbers (for example: add 280 25). Income is money earned. Expenses are money spent or costs such as fuel, parking or food. Never add expenses to income. "
              "none (anything else). "
              "Reply with the tool only, like: week 27, day 2026-10-13, total, add 280 25, none. "
              "Question: " + question)
    tool = ask_gemini(choose).strip().lower()
   # print("Tool chosen:", tool)

    parts = tool.split()

    if parts[0] == "week":
        income, expenses, profit = week_figures(int(parts[1]))
        answer = f"Week {parts[1]}: income £{income:.2f}, expenses £{expenses:.2f}, profit £{profit:.2f}."
    elif parts[0] == "day":
        income, expenses, profit = day_figures(parts[1])
        answer = f"{parts[1]}: income £{income:.2f}, expenses £{expenses:.2f}, profit £{profit:.2f}."
    elif parts[0] == "total":
        income, expenses, profit, tax = total_figures()
        answer = f"Tax year {tax_year} so far: income £{income:.2f}, expenses £{expenses:.2f}, profit £{profit:.2f}, estimated tax £{tax:.2f}."
    elif parts[0] == "add":
        income = abs(float(parts[1]))
        expenses = abs(float(parts[2]))
        sure = input(f"Save today: income £{income:.2f}, expenses £{expenses:.2f}? (yes/no): ")
        if sure.lower() in ["yes", "y"]:
            entry = add_entry(today, income, expenses)
            answer = f"Saved. Today's profit: £{entry['profit']:.2f}."
        else:
            answer = "Not saved."
    else:
        answer = "I can only answer about your income records."


    print("Agent:", answer)

    