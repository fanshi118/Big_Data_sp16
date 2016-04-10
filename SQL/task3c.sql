SELECT DISTINCT hack_license, COUNT(DISTINCT medallion) AS num_taxis_used
FROM trips
GROUP BY hack_license
ORDER BY hack_license ASC;