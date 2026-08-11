from .data_loader import load_raw_orders
from .audit_logger import AuditLogger
from .remediation_agent import RemediationAgent


def main() -> None:
    audit_logger = AuditLogger()
    agent = RemediationAgent(audit_logger)
    raw_df = load_raw_orders()
    clean_df, quarantine_df = agent.remediate(raw_df)

    print(f"Clean records written: {len(clean_df)}")
    print(f"Quarantined records written: {len(quarantine_df)}")
    print("Audit trail created.")


if __name__ == "__main__":
    main()
