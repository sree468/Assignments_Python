-- 1. Extract year from Order_Date.
select extract(Year from Order_Date) from Orders;

-- 2. Extract month from Order_Date.
select extract(month from Order_Date) from Orders;

-- 3. Extract day from Order_Date.
select extract(day from Order_Date) from Orders;

-- 4. Find current date.
 SELECT EXTRACT(date FROM SYSDATE);
-- 5. Find current timestamp.

-- 6. Add 7 days to Order_Date.
select Order_Date+7 from Orders;

-- 7. Subtract 30 days from Order_Date.
select Order_Date-30 from Orders;

-- 8. Find difference between two dates.
SELECT DATE '2026-02-02' - DATE '2026-02-01' AS day_difference
FROM dual;

-- 9. Find number of months between two dates.
-- SELECT months_difference(
--         DATE '2026-02-02',
--         DATE '2026-01-01'
--       ) AS months_difference
-- FROM dual;

-- 10. Find last day of the month.
SELECT LAST_DAY(DATE '2026-02-10') AS last_day_of_month
FROM dual;

-- 11. Get first day of the year.
-- SELECT TRUNC(DATE '2026-02-10', 'MM') AS first_day_of_month
FROM dual;

-- 12. Format date as 'DD-MM-YYYY'.
SELECT TO_CHAR(SYSDATE, 'DD-MM-YYYY') AS formatted_date
FROM dual;

-- 13. Convert string to date.
SELECT TO_DATE('2026-02-10', 'YYYY-MM-DD') AS converted_date
FROM dual;

-- 14. Convert date to string.
SELECT TO_CHAR(SYSDATE, 'YYYY/MM/DD') AS date_string
FROM dual;

-- 15. Find week number of the year.
SELECT TO_CHAR(SYSDATE, 'WW') AS week_number
FROM dual;

-- 16. Find day name from date.
SELECT TO_CHAR(SYSDATE, 'DAY') AS day_name
FROM dual;

-- 17. Find quarter of the year.
SELECT TO_CHAR(SYSDATE, 'Q') AS quarter
FROM dual;

-- 18. Calculate age from DOB.
SELECT TRUNC(MONTHS_BETWEEN(SYSDATE, DATE '2000-02-10') / 12) AS age
FROM dual;

-- 19. Check if date is weekend.

-- 20. Find next Monday after a given date.
SELECT NEXT_DAY(DATE '2026-02-10', 'MONDAY') AS next_monday
FROM dual;