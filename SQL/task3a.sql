SELECT DISTINCT medallion, pickup_datetime
FROM 
(SELECT medallion, pickup_datetime, COUNT(pickup_datetime) AS num_pickups
	FROM trips
	GROUP BY medallion, pickup_datetime) temptrips
WHERE num_pickups>1
ORDER BY medallion ASC;