# SQL

## Task1
Write a SQL query that joins the “trips” and “fares” tables and populates a new table called “alltrips”.

## Task2-a
Find the distribution of fare amounts, i.e., for each amount A, the number of trips that cost A.

## Task2-b
Find the number of trips with a total cost less than $10.

## Task2-c
Find the distribution of the number of passengers.

## Task2-d
Find the total revenue (for all taxis) per day. The revenue should include the fare amount, tips, tax, tolls, surcharges.

## Task2-e
Find the total number of trips for each taxi.

## Task3-a
Is there more than one record for a given taxi at the same time? Find the answer by writing a query.

## Task3-b
For each taxi, what is the percentage of trips without GPS coordinates, i.e., all 4 coordinates are recorded as 0’s?

## Task3-c
Find the number of different taxis used by each driver.

## Task4-a
Compare trips based on vehicle type: WAV, HYB, CNG, LV1, DSE, NRML.

## Task4-b
Compare trips based on medallion type(Named Driver, Owner must drive).

## Task4-c
List the top 10 agents by total revenue.

# MapReduce

## Task1
Write a map-reduce job that joins the 'trips' and 'fare' data (taxi data).

## Task2-a
Find the distribution of fare amounts (fare_amount) for each of the the following ranges: [0,4], [4.01,8], [8.01,12], [12.01, 16], [16.01, 20], [20.01, 24], [24.01, 28], [28.01, 32], [32.01, 36], [36.01, 40], [40.01, 44], [44.01, 48], [48.01, infinite], i.e., for each range, the number of trips whose fare amount falls in the range.

## Task2-b
Find the number of trips that cost less than or equal than $10 (total_amount).

## Task2-c
Find the distribution of the number of passengers, i.e., for each number of passengers A, the number of trips that had A passengers.

## Task2-d
Find the total revenue (for all taxis) and the total amount spent on tolls per day (from pickup_datetime). The revenue should include the fare amount, tips, and surcharges.

## Task2-e
For each taxi (medallion) find the total number of trips and the average number of trips per day. For the average trips per day, use 2 decimal digits. 

## Task2-f
Find the number of different taxis (medallion) used by each driver (license).

## Task3
Write a map-reduce job that joins the output from Task 1 with the vehicle (license) data.

## Task4-a
Compare trips based on vehicle_type (WAV, HYB, CNG, LV1, DSE, NRML).

## Task4-b
List the top 20 agents by total revenue.