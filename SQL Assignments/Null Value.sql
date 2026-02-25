Gemini said
1. Replace NULL price with 0.
SELECT NVL(Price, 0) FROM Orders;

2. Replace NULL Customer_Name with 'Unknown'.
SELECT NVL(customer_name, 'Unknown') FROM orders;

3. Count NULL values in Product_Name.
SELECT COUNT(*) AS null_count FROM orders WHERE product_name IS NULL;

4. Find rows where Order_Date is NULL.
SELECT * FROM Orders WHERE ORDER_DATE IS NULL;

5. Use COALESCE to return first non-null value.
SELECT COALESCE(PRODUCT_NAME, 'Unknown') FROM Orders;

6. Use NVL to replace NULL values.
SELECT NVL(CUSTOMER_NAME, 'sree') FROM Orders;

7. Use IFNULL function.
SELECT NVL(Quantity, 0) FROM Orders;

8. Check if column is NULL.
SELECT * FROM Orders WHERE Quantity IS NULL;

9. Check if column is NOT NULL.
SELECT * FROM Orders WHERE Quantity IS NOT NULL;

10. Use NULLIF between two columns.
SELECT NULLIF(Quantity, Expected_Quantity) FROM Orders;

11. Replace blank values with NULL.
SELECT NULLIF(Customer_Name, ' ') AS name_fixed FROM Orders;

12. Count non-null values.
SELECT COUNT(Quantity) FROM Orders;

13. Filter records where price is NULL or 0.
SELECT * FROM products WHERE Unit_Price IS NULL OR Unit_Price = 0;

14. Use CASE to handle NULL values.
SELECT CASE WHEN Unit_Price IS NULL THEN 0 ELSE Unit_Price END AS correct_price FROM Products;

15. Compare NULL values properly.
SELECT * FROM Products WHERE price IS NULL;

16. Handle NULL in aggregation.
SELECT SUM(NVL(Unit_Price, 0)) AS total_price FROM Orders;

17. Find average excluding NULL values.
SELECT AVG(Unit_Price) FROM Orders;

18. Find sum ignoring NULL values.
SELECT SUM(prices) AS total_price FROM Products;

19. Identify columns containing NULL using metadata.
SELECT column_name, nullable FROM user_tab_columns WHERE table_name = 'ORDERS' AND nullable = 'Y';

20. Convert NULL to default system date.
SELECT NVL(order_date, SYSDATE) AS Order_fixed_date FROM Orders;