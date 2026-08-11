-- Audit report for remediation actions taken on customer orders
SELECT
    rule,
    action,
    reason,
    COUNT(*) AS event_count
FROM audit_log
GROUP BY rule, action, reason
ORDER BY event_count DESC;
