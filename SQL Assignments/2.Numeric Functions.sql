-- 1. Round Unit_Price to 2 decimal places.
SELECT ROUND(Unit_Price, 2) AS "rounded price"
FROM Orders;

-- 2. Find total sales per order.
select sum(Quantity*Unit_Price) as "total sales" from Orders;

-- 3. Calculate average order value.
select avg(Quantity*Unit_Price) as "average order" from Orders;

-- 4. Find highest product price.
select max(Unit_Price) as "highest product price" from Orders;

-- 5. Find lowest product price.
select min(Unit_Price) as "mimimum product price" from Orders;

-- 6. Calculate percentage discount applied.
SELECT 
  ((1000 - 850) / 1000.0) * 100 AS discount_percentage;

-- 7. Find modulus of Quantity divided by 2.
select mod(Quantity,2) from Orders;

-- 8. Convert negative values to positive.
select abs(floor(Unit_Price)) from Orders;

-- 9. Truncate price without rounding.
-- 10. Find square root of total sales.
select sqrt(Unit_Price * Quantity) AS "total sales" from Orders;

-- 11. Calculate exponential value of a number.
SELECT EXP(2);

-- 12. Calculate power of 2^5.
select power(2,5);

-- 13. Find absolute difference between two prices.
select abs(2-5);

-- 14. Calculate sales growth percentage.

-- 15. Find random number between 1 and 100.

-- 16. Divide total sales by number of orders.
SELECT 
    SUM(Unit_Price * Quantity) / COUNT(*) AS avg_sales_per_order
FROM Orders;

-- 17. Find ceiling value of price.
select ceil(2.6);
-- 18. Find floor value of price.
select floor(2.6);

-- 19. Convert decimal to integer.
SELECT ceil(12.78) AS result;

-- 20. Calculate compound interest.
SELECT 
    (10000 * POWER((1 + 5/100), 2)) - 10000 AS compound_interest;