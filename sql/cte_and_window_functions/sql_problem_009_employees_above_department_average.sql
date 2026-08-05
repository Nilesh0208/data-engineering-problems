/*
SQL Problem 009:
Find Employees Earning More Than Their Department Average

Objective:
Return employees whose salary is greater than the average salary
of their own department.

Requirements:
1. Calculate the average salary for every department.
2. Compare each employee salary with that department average.
3. Return only employees earning above the department average.
4. Show the salary difference from the department average.
5. Sort results by department and salary descending.

Concepts:
- GROUP BY
- AVG()
- CTE
- INNER JOIN
- Department-level aggregation
- Numeric comparison
*/


DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;


CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);


CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INTEGER NOT NULL,
    salary NUMERIC(12, 2) NOT NULL,

    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


INSERT INTO departments (
    department_id,
    department_name
)
VALUES
    (1, 'Engineering'),
    (2, 'Finance'),
    (3, 'Marketing');


INSERT INTO employees (
    employee_id,
    employee_name,
    department_id,
    salary
)
VALUES
    (101, 'Amit Sharma', 1, 120000.00),
    (102, 'Priya Patil', 1, 100000.00),
    (103, 'Rahul Joshi', 1, 80000.00),

    (201, 'Neha Verma', 2, 110000.00),
    (202, 'Rohan Mehta', 2, 90000.00),
    (203, 'Kiran Shah', 2, 70000.00),

    (301, 'Anjali Deshmukh', 3, 95000.00),
    (302, 'Vikas More', 3, 85000.00),
    (303, 'Pooja Nair', 3, 75000.00),
    (304, 'Sneha Kulkarni', 3, 65000.00);


WITH department_averages AS (
    SELECT
        department_id,
        AVG(salary) AS average_salary
    FROM employees
    GROUP BY department_id
)

SELECT
    e.employee_id,
    e.employee_name,
    d.department_name,
    e.salary,

    ROUND(
        da.average_salary,
        2
    ) AS department_average_salary,

    ROUND(
        e.salary - da.average_salary,
        2
    ) AS salary_above_average

FROM employees AS e

INNER JOIN department_averages AS da
    ON e.department_id = da.department_id

INNER JOIN departments AS d
    ON e.department_id = d.department_id

WHERE e.salary > da.average_salary

ORDER BY
    d.department_name,
    e.salary DESC;