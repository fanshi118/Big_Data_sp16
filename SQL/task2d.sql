SELECT date(pickup_datetime) AS day, 
SUM(fare_amount+tip_amount+mta_tax+tolls_amount+surcharge) AS total_revenue
FROM fares
GROUP BY day
ORDER BY day ASC;