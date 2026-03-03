CREATE TABLE employees_new (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(10),
    city VARCHAR2(10),
    salary number(10,2) check (salary > 0)
);
INSERT INTO employees_new VALUES (1, 'Charan', 'Bangalore', 1000);
INSERT INTO employees_new VALUES (2, 'Ravi', 'Hyderabad', 4000);
INSERT INTO employees_new VALUES (3, 'Anil', 'Chennai', 12453);
INSERT INTO employees_new VALUES (4, 'Neha', 'Mumbai', 234567);
INSERT INTO employees_new VALUES (5, 'John', 'Delhi', 3245647);
select * from EMPLOYEES_NEW;