from tracker import month_label

def test_april_1_to_5():
    assert month_label("2026-04-05") == "2026-04 (1-5)"

def test_april_6_to_30():
    assert month_label("2026-04-06") == "2026-04 (6-30)"
    assert month_label("2026-04-30") == "2026-04 (6-30)"

def test_normal_month():
    assert month_label("2026-05-01") == "2026-05"
    assert month_label("2026-06-15") == "2026-06"
    assert month_label("2026-07-31") == "2026-07"