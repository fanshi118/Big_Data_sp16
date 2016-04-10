SELECT medallion_type,
COUNT(f.medallion) AS total_trips,
SUM(f.fare_amount) AS total_revenue,
CONCAT(SUM(f.tip_amount/f.fare_amount)/COUNT(f.medallion)*100,'%') 
AS avg_tip_percentage
FROM medallions m, fares f
WHERE m.medallion=f.medallion
GROUP BY medallion_type
ORDER BY medallion_type ASC;