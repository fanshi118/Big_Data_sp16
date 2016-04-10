SELECT DISTINCT medallion,
CONCAT(SUM(CASE WHEN (pickup_longitude=0 
	AND pickup_latitude=0 
	AND dropoff_longitude=0 
	AND dropoff_latitude=0)
	THEN 1 ELSE 0 END)/COUNT(*)*100, '%') 
AS percentage_of_trips
FROM trips
GROUP BY medallion
ORDER BY medallion ASC;