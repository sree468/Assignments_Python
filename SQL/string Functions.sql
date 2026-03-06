-- Convert all customer names to uppercase

SELECT UPPER(Customer_Name) AS customer_name_upper
FROM Orders;

-- Extract the first 5 characters from Product_Name
SELECT SUBSTRING(Product_Name, 1, 5) AS first_5_chars
FROM Orders;

-- Find the length of each Customer_Name
SELECT Customer_Name, LENGTH(Customer_Name) AS name_length
FROM Orders;

-- Replace the word "Rice" with "Premium Rice"
SELECT REPLACE(Product_Name, 'Rice', 'Premium Rice') AS updated_product
FROM Orders;

-- Remove leading and trailing spaces from Customer_Name
SELECT TRIM(Customer_Name) AS trimmed_name
FROM Orders;

-- Concatenate First_Name and Last_Name as Full_Name
SELECT CONCAT(First_Name, ' ', Last_Name) AS Full_Name
FROM Customers;

-- Find customers whose names start with 'A'
SELECT *
FROM Orders
WHERE Customer_Name LIKE 'A%';

-- Extract domain name from Email_ID
SELECT SUBSTRING(Email_ID, POSITION('@' IN Email_ID) + 1) AS domain
FROM Customers;

-- Find the position of '@' in Email_ID
SELECT POSITION('@' IN Email_ID) AS at_position
FROM Customers;

--Reverse the Product_Name
SELECT REVERSE(Product_Name) AS reversed_product
FROM Orders;

-- Capitalize first letter of each word in Product_Name
SELECT INITCAP(Product_Name) AS formatted_product
FROM Orders;

-- Extract the last 3 characters from Order_ID
SELECT RIGHT(Order_ID, 3) AS last_3_digits
FROM Orders;

-- Count how many times letter 'a' appears in Customer_Name
SELECT Customer_Name,
       LENGTH(LOWER(Customer_Name))
     - LENGTH(REPLACE(LOWER(Customer_Name), 'a', '')) AS a_count
FROM Orders;

-- Mask the last 4 digits of a phone number
SELECT CONCAT(LEFT(Phone_Number, LENGTH(Phone_Number) - 4), 'XXXX') AS masked_phone
FROM Customers;

-- Split Full_Name into First_Name and Last_Name
SELECT
  SUBSTRING(Full_Name, 1, POSITION(' ' IN Full_Name) - 1) AS First_Name,
  SUBSTRING(Full_Name, POSITION(' ' IN Full_Name) + 1) AS Last_Name
FROM Customers;

-- Remove all special characters from Product_Code
SELECT REGEXP_REPLACE(Product_Code, '[^A-Za-z0-9]', '') AS cleaned_code
FROM Products;

-- Compare two columns ignoring case sensitivity
SELECT *
FROM Orders
WHERE LOWER(Customer_Name) = LOWER('ravi kumar');

-- Find customers whose name contains 'kumar'
SELECT *
FROM Orders
WHERE LOWER(Customer_Name) LIKE '%kumar%';

-- Pad Order_ID with leading zeros (6 digits)
SELECT LPAD(Order_ID, 6, '0') AS padded_order_id
FROM Orders;

-- Extract substring between two characters
SELECT SUBSTRING(col,
                 POSITION('(' IN col) + 1,
                 POSITION(')' IN col) - POSITION('(' IN col) - 1) AS extracted_text
FROM table_name;