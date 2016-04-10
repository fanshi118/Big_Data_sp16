SELECT fare_amount AS amount, COUNT(*) AS num_trips
FROM fares
GROUP BY amount
ORDER BY amount ASC;