select * from orders;
-- Find sine value of an angle.
select sin(1);
-- Find cosine value of an angle.
select cos(0);
-- Find tangent value.
select tan(45);
-- Convert degrees to radians.
SELECT RADIANS(180) AS radians_value
FROM dual;
-- Convert radians to degrees.
SELECT DEGREES(3.14159265358979) AS degrees_value
FROM dual;
-- Find logarithm (base 10) of a number.
select log(10,2);
-- Find natural log of a number.
select ln(2);
-- Find square of a number.
SELECT POWER(10, 2) AS square_value FROM dual;
-- Find cube of a number.
SELECT POWER(5, 3) AS cube_value FROM dual;
-- Calculate factorial of a number.

-- Find greatest value among three numbers.
SELECT
  CASE
    WHEN 10 >= 20 AND 10 >= 30 THEN 10
    WHEN 20 >= 30 THEN 20
    ELSE 30
  END AS max_value
FROM dual;
-- Find least value among three numbers.
SELECT
  CASE
    WHEN 10 <= 20 AND 10 <= 30 THEN 10
    WHEN 20 <= 30 THEN 20
    ELSE 30
  END AS min_value
FROM dual;
-- Calculate variance of sales
select VARIANCE(Quantity*Unit_Price) from Orders;
-- Calculate standard deviation of sales.
select stddev(Quantity*Unit_Price) from Orders;
-- Find average deviation.
-- Calculate geometric mean.
-- Calculate harmonic mean.
-- Find sum of squares.
SELECT SUM(POWER(Quantity * Unit_Price, 2)) AS sum_of_squares
FROM Orders;
-- Calculate correlation between two columns.
SELECT CORR(Quantity, Unit_Price) AS correlation_value
FROM Orders;
-- Calculate regression slope.
SELECT REGR_SLOPE(Quantity * Unit_Price, Quantity) AS regression_slope
FROM Orders;