SELECT agent_name, SUM(f.fare_amount) AS total_revenue
FROM medallions m, fares f
WHERE m.medallion=f.medallion
GROUP BY agent_name
ORDER BY total_revenue DESC, agent_name ASC
LIMIT 10;