-- Data quality summary for cleaned customer orders.
SELECT
    order_status,
    COUNT(*) AS record_count,
    AVG(CAST(order_amount AS numeric)) AS avg_order_amount,
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date
FROM clean_orders
GROUP BY order_status
ORDER BY order_status;
