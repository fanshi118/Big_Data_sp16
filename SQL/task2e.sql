SELECT medallion, COUNT(*) AS num_trips
FROM trips
GROUP BY medallion
ORDER BY medallion ASC;