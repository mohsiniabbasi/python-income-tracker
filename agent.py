import requests
from dotenv import load_dotenv
import os
from tracker import week_figures, day_figures, total_figures,today, week, tax_year

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

while True:
    question = input("You (x to exit): ")
    if question == "x":
        break

    choose = ("Today is " + today.strftime("%A %Y-%m-%d") + ". This is week " + str(week) + " of the tax year. "
              "Pick the tool for the question. Tools: "
              "week N (figures for tax-year week N), "
              "day YYYY-MM-DD (figures for one date), "
              "total (totals and tax estimate for this tax year), "
              "none (anything else). "
              "Reply with the tool only, like: week 27, day 2026-10-13, total, none. "
              "Question: " + question)
    tool = ask_gemini(choose).strip().lower()
    print("Tool chosen:", tool)

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
    else:
        answer = "I can only answer about your income records."


    print("Agent:", answer)

    