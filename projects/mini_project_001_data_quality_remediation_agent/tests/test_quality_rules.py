import pandas as pd
from src.quality_rules import (
    rule_missing_order_id,
    rule_missing_customer_id,
    rule_negative_order_amount,
    rule_invalid_order_status,
    rule_invalid_order_date,
    find_quality_issues,
)


def test_rule_missing_order_id():
    assert rule_missing_order_id({"order_id": ""})
    assert not rule_missing_order_id({"order_id": "100"})


def test_rule_missing_customer_id():
    assert rule_missing_customer_id({"customer_id": ""})
    assert not rule_missing_customer_id({"customer_id": "501"})


def test_rule_negative_order_amount():
    assert rule_negative_order_amount({"order_amount": "-10"})
    assert rule_negative_order_amount({"order_amount": "bad"})
    assert not rule_negative_order_amount({"order_amount": "20"})


def test_rule_invalid_order_status():
    assert rule_invalid_order_status({"order_status": "INVALID"})
    assert not rule_invalid_order_status({"order_status": "completed"})


def test_rule_invalid_order_date():
    assert rule_invalid_order_date({"order_date": "2027-01-01"})
    assert rule_invalid_order_date({"order_date": "not-a-date"})
    assert not rule_invalid_order_date({"order_date": "2026-01-01"})


def test_find_quality_issues_duplicate_order_id():
    record = {"order_id": "1001", "customer_id": "501", "order_amount": "10", "order_status": "NEW", "order_date": "2026-01-01"}
    issues = find_quality_issues(record, seen_order_ids={"1001"})
    assert any(issue["rule"] == "duplicate_order_id" for issue in issues)
