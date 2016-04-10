CREATE VIEW alltrips AS
SELECT
	t.medallion, t.hack_license, t.vendor_id, t.pickup_datetime, 
	t.rate_code, t.store_and_fwd_flag, t.dropoff_datetime, t.passenger_count, 
	t.trip_time_in_secs, t.trip_distance, t.pickup_longitude, t.pickup_latitude, 
	t.dropoff_longitude, t.dropoff_latitude,
	f.payment_type, f.fare_amount, f.surcharge, f.mta_tax,
	f.tip_amount, f.tolls_amount, f.total_amount
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

SELECT * FROM alltrips;