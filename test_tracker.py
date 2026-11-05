import tracker
from tracker import month_label, week_and_tax_year, work_out_tax
from datetime import date

def test_april_1_to_5():
    assert month_label("2026-04-05") == "2026-04 (1-5)"

def test_april_6_to_30():
    assert month_label("2026-04-06") == "2026-04 (6-30)"
    assert month_label("2026-04-30") == "2026-04 (6-30)"

def test_normal_month():
    assert month_label("2026-05-01") == "2026-05"
    assert month_label("2026-06-15") == "2026-06"
    assert month_label("2026-07-31") == "2026-07"

def test_first_day_of_tax_year():
    assert week_and_tax_year(date(2026, 4, 6)) == (1, 2026)
    assert week_and_tax_year(date(2026, 4, 5)) == (53, 2025)

def test_tax_full_year_30000():
    assert round(work_out_tax(30000, 52), 2) == 4531.80

def test_missing_dates():
    tracker.entries = [{"date": "2026-10-20", "tax_year": 2026},
                       {"date": "2026-10-23", "tax_year": 2026}]
    tracker.tax_year = 2026
    tracker.today = date(2026, 10, 24)
    assert tracker.missing_dates() == [date(2026,10,21) , date(2026,10,22)]

def test_tax_full_year_50270():
    assert round(work_out_tax(50270, 52), 2) == 9802.00

def test_tax_full_year_60000():
    assert round(work_out_tax(60000, 52), 2) == 13888.60