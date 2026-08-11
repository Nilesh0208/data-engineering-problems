import pandas as pd
from pathlib import Path
from src.audit_logger import AuditLogger
from src.remediation_agent import RemediationAgent


def test_remediation_agent_quarantines_critical(tmp_path):
    input_data = [
        {"order_id": "1001", "customer_id": "", "order_amount": "50", "order_status": "NEW", "order_date": "2026-01-01", "updated_at": "2026-01-01 10:00:00"},
        {"order_id": "1002", "customer_id": "501", "order_amount": "100", "order_status": "completed", "order_date": "2026-01-02", "updated_at": "2026-01-02 11:00:00"},
    ]
    raw_df = pd.DataFrame(input_data)
    audit_path = tmp_path / "audit_log.csv"
    agent = RemediationAgent(AuditLogger())
    agent.audit_logger._path = audit_path
    clean_df, quarantine_df = agent.remediate(raw_df)

    assert len(clean_df) == 1
    assert len(quarantine_df) == 1
    assert quarantine_df.iloc[0]["order_id"] == "1001"
    assert clean_df.iloc[0]["order_id"] == "1002"


def test_remediation_agent_deduplicates_keep_latest(tmp_path):
    input_data = [
        {"order_id": "1001", "customer_id": "501", "order_amount": "50", "order_status": "NEW", "order_date": "2026-01-01", "updated_at": "2026-01-01 10:00:00"},
        {"order_id": "1001", "customer_id": "501", "order_amount": "55", "order_status": "NEW", "order_date": "2026-01-01", "updated_at": "2026-01-01 12:00:00"},
    ]
    raw_df = pd.DataFrame(input_data)
    audit_path = tmp_path / "audit_log.csv"
    agent = RemediationAgent(AuditLogger())
    agent.audit_logger._path = audit_path
    clean_df, quarantine_df = agent.remediate(raw_df)

    assert len(clean_df) == 1
    assert clean_df.iloc[0]["order_amount"] == "55"
    assert clean_df.iloc[0]["updated_at"] == "2026-01-01 12:00:00"
    assert quarantine_df.empty


def test_remediation_agent_handles_invalid_dates_and_nat(tmp_path):
    input_data = [
        {"order_id": "1003", "customer_id": "501", "order_amount": "120", "order_status": "NEW", "order_date": "not-a-date", "updated_at": "not-a-time"},
    ]
    raw_df = pd.DataFrame(input_data)
    audit_path = tmp_path / "audit_log.csv"
    agent = RemediationAgent(AuditLogger())
    agent.audit_logger._path = audit_path
    clean_df, quarantine_df = agent.remediate(raw_df)

    assert len(clean_df) == 1
    assert clean_df.iloc[0]["order_date"] == ""
    assert clean_df.iloc[0]["updated_at"] == ""
    assert quarantine_df.empty
