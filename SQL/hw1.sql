# Task 1
## create alltrips virtual table
CREATE VIEW alltrips AS
SELECT
	t.*,
	f.payment_type,
	f.fare_amount,
	f.surcharge,
	f.mta_tax,
	f.tip_amount,
	f.tolls_amount,
	f.total_amount
FROM trips t
INNER JOIN fares f
ON t.medallion=f.medallion
AND t.hack_license=f.hack_license
AND t.vendor_id=f.vendor_id
AND t.pickup_datetime=f.pickup_datetime
ORDER BY
	t.medallion ASC,
	t.hack_license ASC,
	t.vendor_id ASC,
	t.pickup_datetime ASC,
	t.pickup_longitude ASC;
## select all from alltrips
SELECT * FROM alltrips;

# Task 2
## a
SELECT fare_amount AS amount, COUNT(*) AS num_trips
FROM fares
GROUP BY amount
ORDER BY amount ASC;
## b
SELECT COUNT(*) AS num_trips
FROM fares
WHERE fare_amount<10;
## c
SELECT passenger_count AS number_of_passengers, COUNT(*) AS num_trips
FROM trips
GROUP BY number_of_passengers
ORDER BY number_of_passengers ASC;
## d
SELECT date(pickup_datetime) AS day, 
SUM(fare_amount+tip_amount+mta_tax+tolls_amount+surcharge) AS total_revenue
FROM fares
GROUP BY day
ORDER BY day ASC;
## e
SELECT medallion, COUNT(*) AS num_trips
FROM trips
GROUP BY medallion
ORDER BY medallion ASC;

# Task 3
## a
SELECT DISTINCT medallion, pickup_datetime
FROM 
(SELECT medallion, pickup_datetime, COUNT(pickup_datetime) AS num_pickups
	FROM trips
	GROUP BY medallion, pickup_datetime) temptrips
WHERE num_pickups>1
ORDER BY medallion ASC;
## b
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
## c
SELECT DISTINCT hack_license, COUNT(DISTINCT medallion) AS num_taxis_used
FROM trips
GROUP BY hack_license
ORDER BY hack_license ASC;

# Task 4
## a
### create allfares virtual table
CREATE VIEW allfares AS
SELECT 
m.*,
f.hack_license,
f.vendor_id,
f.pickup_datetime,
f.payment_type,
f.fare_amount,
f.surcharge,
f.mta_tax,
f.tip_amount,
f.tolls_amount,
f.total_amount
FROM medallions m 
RIGHT JOIN fares f 
ON f.medallion=m.medallion;
### query revenue and tip percentage
SELECT vehicle_type,
COUNT(f.medallion) AS total_trips,
SUM(f.fare_amount) AS total_revenue,
CONCAT(SUM(f.tip_amount)/SUM(f.fare_amount)*100/COUNT(f.medallion),'%') 
AS avg_tip_percentage
FROM medallions m, fares f
WHERE m.medallion=f.medallion
GROUP BY vehicle_type
ORDER BY vehicle_type ASC;
## b
SELECT medallion_type,
COUNT(f.medallion) AS total_trips,
SUM(f.fare_amount) AS total_revenue,
CONCAT(SUM(f.tip_amount)/SUM(f.fare_amount)*100/COUNT(f.medallion),'%') 
AS avg_tip_percentage
FROM medallions m, fares f
WHERE m.medallion=f.medallion
GROUP BY medallion_type
ORDER BY medallion_type ASC;
## c
SELECT agent_name, SUM(f.fare_amount) AS total_revenue
FROM medallions m, fares f
WHERE m.medallion=f.medallion
GROUP BY agent_name
ORDER BY total_revenue DESC, agent_name ASC
LIMIT 10;