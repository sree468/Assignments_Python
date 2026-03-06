-- M1. Display employee_id, first_name, last_name, and a new column full_name that is first_name and last_name concatenated with a comma between them (e.g., "John, Doe").
select employee_id,first_name,last_name,first_name || ' , ' || last_name as full_name from employees;
-- M2. List employee_id, salary, and a column bonus_10_pct showing 10% of salary (salary * 0.10).
SELECT employee_id, salary, (salary * 1.10) as bonus_10_pct from employees;
-- M3. Show employee_id, hire_date, and a literal column record_type with value 'Employee' for every row.
SELECT employee_id, hire_date,'Employee' as status from employees;
--M4. For each employee, display email and a column email_domain set to the literal '@company.com'.
SELECT employee_id,email,'@company.com' as email_domain from employees;
--M5. List employee_id, salary, commission_pct, and effective_commission where effective_commission is NVL(commission_pct, 0).
SELECT employee_id, salary, commission_pct,NVL(commission_pct, 0) as effective_commission from employees;
--M6. Display first_name, last_name, and a column initials formed by the first character of first_name and the first character of last_name (e.g., "JD").
select first_name, last_name, substr(first_name,1,1)||substr(last_name,1,1) as nick_name from employees;
--M7. Show employee_id, salary, and annual_salary as salary * 12, and also annual_plus_bonus as salary * 12 * 1.1 (10% bonus).
SELECT employee_id, salary,salary * 12 as annual_salary,salary * 12 * 1.1 as annual_plus_bonus from employees;
--M8. List all columns from hr.departments using explicit column names (department_id, department_name, manager_id, location_id).
select department_id, department_name, manager_id, location_id from DEPARTMENTS;
--M9. From hr.employees, select employee_id and a column description that is the literal 'Emp#' concatenated with employee_id (cast to string if needed: use TO_CHAR(employee_id)).
SELECT employee_id,'Emp#' || to_char(employee_id) as emp_id from EMPLOYEES;
--M10. Display job_id, salary, and a column salary_band that is the literal 'Standard' for every row.
SELECT job_id, salary,'Standard' as salary_band from EMPLOYEES;
--M11. List employee_id, first_name, last_name, and a column display_name as "Last, First" (last_name, comma space, first_name).
SELECT employee_id, first_name, last_name,last_name || ',' || first_name from employees;
--M12. Show department_id from hr.departments and a literal 1 as column sort_order.
SELECT department_id, '1' as sort_order from DEPARTMENTS;
--M13. From hr.employees, display salary and monthly_net as salary * 0.85 (assuming 15% tax).
SELECT salary,salary * 0.85 as monthly_net from EMPLOYEES;
--M14. List employee_id, commission_pct, and commission_display where NULL commission_pct is shown as 0 using NVL.
SELECT employee_id,commission_pct,NVL(commission_pct, 0) AS commission_display FROM employees;
--M15. Display first_name, last_name, salary, and a column compensation that is salary * (1 + NVL(commission_pct, 0)).
SELECT first_name, last_name, salary,salary * (1 + NVL(commission_pct, 0)) as compensation from employees;
--M16. From hr.departments, list department_name and a literal column region with value 'HQ'.
SELECT department_name,'HQ' as region from DEPARTMENTS;
--M17. Show employee_id, hire_date, and a column years_label with literal 'Years of service'.
SELECT  employee_id, hire_date,'Years of service' as years_label from EMPLOYEES;
--M18. List employee_id, salary, and double_salary as salary * 2.
SELECT employee_id, salary,salary * 2 as double_salary from EMPLOYEES;
--M19. From hr.employees, display manager_id and a column has_manager that is the literal 'Yes' when manager_id is not null and 'No' when manager_id is null (use NVL2: NVL2(manager_id, 'Yes', 'No')).
SELECT manager_id,
    case 
        when manager_id is not null then 'Yes'
        else 'NO'
    end as has_manager
from employees;
--M20. Show department_id, department_name from hr.departments, and a calculated column dept_code as the first 3 characters of department_name (use SUBSTR).
SELECT department_id, department_name,substr(department_name,1,3) as dept_code from DEPARTMENTS;
--------------------------------------------HARD-----------------------------------------------------------
--












































































