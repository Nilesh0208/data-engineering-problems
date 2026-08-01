/*
SQL Problem 001: Top Two Highest-Paid Employees in Each Department

Objective:
Return employees with the top two distinct salaries in every department.

Concepts:
- CREATE TABLE
- INSERT
- JOIN
- Common Table Expression
- DENSE_RANK()
- PARTITION BY
- ORDER BY

Important:
DENSE_RANK is used so employees with the same salary receive the same rank.
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
    (102, 'Priya Patil', 1, 110000.00),
    (103, 'Rahul Joshi', 1, 110000.00),
    (104, 'Sneha Kulkarni', 1, 95000.00),

    (201, 'Neha Verma', 2, 105000.00),
    (202, 'Rohan Mehta', 2, 98000.00),
    (203, 'Kiran Shah', 2, 90000.00),

    (301, 'Anjali Deshmukh', 3, 85000.00),
    (302, 'Vikas More', 3, 85000.00),
    (303, 'Pooja Nair', 3, 80000.00);


WITH ranked_employees AS (
    SELECT
        e.employee_id,
        e.employee_name,
        d.department_name,
        e.salary,
        DENSE_RANK() OVER (
            PARTITION BY e.department_id
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM employees AS e
    INNER JOIN departments AS d
        ON e.department_id = d.department_id
)
SELECT
    employee_id,
    employee_name,
    department_name,
    salary,
    salary_rank
FROM ranked_employees
WHERE salary_rank <= 2
ORDER BY
    department_name,
    salary_rank,
    employee_name;