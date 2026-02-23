-- ================================================================================
--                     SQL PRACTICE EXAMPLES
-- ================================================================================

-- ================================================================================
-- DATABASE SETUP
-- ================================================================================

CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

-- Create Departments table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(15,2)
);

-- Create Employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    hire_date DATE NOT NULL,
    job_title VARCHAR(50),
    salary DECIMAL(10,2) NOT NULL,
    commission DECIMAL(10,2),
    manager_id INT,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

-- Create Projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Create Employee_Projects (Many-to-Many)
CREATE TABLE employee_projects (
    emp_id INT,
    project_id INT,
    role VARCHAR(50),
    hours_worked INT,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);


-- ================================================================================
-- INSERT SAMPLE DATA
-- ================================================================================

INSERT INTO departments (dept_name, location, budget) VALUES
('Engineering', 'New York', 500000),
('Sales', 'Chicago', 300000),
('HR', 'Boston', 200000),
('Marketing', 'Los Angeles', 250000),
('Finance', 'New York', 400000);

INSERT INTO employees (first_name, last_name, email, hire_date, job_title, salary, manager_id, dept_id) VALUES
('John', 'Smith', 'john.smith@company.com', '2020-01-15', 'Engineering Manager', 95000, NULL, 1),
('Jane', 'Doe', 'jane.doe@company.com', '2020-03-20', 'Software Engineer', 75000, 1, 1),
('Bob', 'Wilson', 'bob.wilson@company.com', '2019-06-10', 'Senior Engineer', 85000, 1, 1),
('Alice', 'Brown', 'alice.brown@company.com', '2021-02-01', 'Sales Manager', 80000, NULL, 2),
('Charlie', 'Davis', 'charlie.davis@company.com', '2021-05-15', 'Sales Rep', 55000, 4, 2),
('Eva', 'Martinez', 'eva.martinez@company.com', '2020-09-01', 'HR Manager', 70000, NULL, 3),
('Frank', 'Garcia', 'frank.garcia@company.com', '2022-01-10', 'Recruiter', 50000, 6, 3),
('Grace', 'Lee', 'grace.lee@company.com', '2019-11-20', 'Marketing Manager', 78000, NULL, 4),
('Henry', 'Taylor', 'henry.taylor@company.com', '2021-08-15', 'Content Writer', 52000, 8, 4),
('Ivy', 'Anderson', 'ivy.anderson@company.com', '2020-04-01', 'Finance Manager', 90000, NULL, 5);

INSERT INTO projects (project_name, start_date, end_date, budget, dept_id) VALUES
('Website Redesign', '2023-01-01', '2023-06-30', 100000, 1),
('Mobile App', '2023-03-01', '2023-12-31', 200000, 1),
('Sales Campaign', '2023-02-01', '2023-04-30', 50000, 2),
('Employee Portal', '2023-04-01', '2023-09-30', 80000, 3),
('Brand Refresh', '2023-05-01', '2023-08-31', 75000, 4);

INSERT INTO employee_projects (emp_id, project_id, role, hours_worked) VALUES
(1, 1, 'Project Lead', 200),
(2, 1, 'Developer', 400),
(3, 1, 'Developer', 350),
(2, 2, 'Developer', 300),
(3, 2, 'Lead Developer', 450),
(4, 3, 'Campaign Lead', 150),
(5, 3, 'Sales Support', 200),
(6, 4, 'Project Owner', 100),
(7, 4, 'Developer', 250),
(8, 5, 'Creative Lead', 180),
(9, 5, 'Content Creator', 220);


-- ================================================================================
-- BASIC QUERIES
-- ================================================================================

-- Select all employees
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- With alias
SELECT
    first_name AS "First Name",
    last_name AS "Last Name",
    salary AS "Annual Salary"
FROM employees;

-- Distinct departments
SELECT DISTINCT dept_id FROM employees;

-- Order by salary descending
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;

-- Limit results
SELECT * FROM employees LIMIT 5;


-- ================================================================================
-- WHERE CLAUSE
-- ================================================================================

-- Simple condition
SELECT * FROM employees WHERE salary > 70000;

-- Multiple conditions (AND)
SELECT * FROM employees
WHERE dept_id = 1 AND salary > 70000;

-- Multiple conditions (OR)
SELECT * FROM employees
WHERE dept_id = 1 OR dept_id = 2;

-- IN operator
SELECT * FROM employees
WHERE dept_id IN (1, 2, 3);

-- BETWEEN operator
SELECT * FROM employees
WHERE salary BETWEEN 60000 AND 80000;

-- LIKE operator
SELECT * FROM employees
WHERE first_name LIKE 'J%';  -- Starts with J

SELECT * FROM employees
WHERE email LIKE '%@company.com';  -- Ends with @company.com

-- IS NULL
SELECT * FROM employees
WHERE manager_id IS NULL;  -- Top-level managers


-- ================================================================================
-- AGGREGATE FUNCTIONS
-- ================================================================================

-- Count all employees
SELECT COUNT(*) AS total_employees FROM employees;

-- Sum of all salaries
SELECT SUM(salary) AS total_payroll FROM employees;

-- Average salary
SELECT AVG(salary) AS avg_salary FROM employees;

-- Min and Max salary
SELECT
    MIN(salary) AS lowest_salary,
    MAX(salary) AS highest_salary
FROM employees;

-- Count by department
SELECT
    dept_id,
    COUNT(*) AS emp_count,
    AVG(salary) AS avg_salary,
    SUM(salary) AS total_salary
FROM employees
GROUP BY dept_id;

-- Having clause (filter groups)
SELECT
    dept_id,
    COUNT(*) AS emp_count,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
HAVING COUNT(*) >= 2;


-- ================================================================================
-- JOINS
-- ================================================================================

-- INNER JOIN: Employees with their departments
SELECT
    e.first_name,
    e.last_name,
    e.salary,
    d.dept_name,
    d.location
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- LEFT JOIN: All employees (including those without dept)
SELECT
    e.first_name,
    e.last_name,
    d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- RIGHT JOIN: All departments (including those without employees)
SELECT
    e.first_name,
    e.last_name,
    d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- SELF JOIN: Employees with their managers
SELECT
    e.first_name AS employee,
    e.last_name AS employee_last,
    m.first_name AS manager,
    m.last_name AS manager_last
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- Multiple joins: Employees, departments, and projects
SELECT
    e.first_name,
    e.last_name,
    d.dept_name,
    p.project_name,
    ep.role
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
JOIN employee_projects ep ON e.emp_id = ep.emp_id
JOIN projects p ON ep.project_id = p.project_id;


-- ================================================================================
-- SUBQUERIES
-- ================================================================================

-- Employees earning above average
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Employees in Engineering department
SELECT first_name, last_name
FROM employees
WHERE dept_id = (
    SELECT dept_id FROM departments WHERE dept_name = 'Engineering'
);

-- Employees working on any project
SELECT first_name, last_name
FROM employees
WHERE emp_id IN (
    SELECT DISTINCT emp_id FROM employee_projects
);

-- Employees NOT working on any project
SELECT first_name, last_name
FROM employees
WHERE emp_id NOT IN (
    SELECT DISTINCT emp_id FROM employee_projects
);

-- Correlated subquery: Employees earning more than dept average
SELECT e.first_name, e.last_name, e.salary, e.dept_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id
);


-- ================================================================================
-- WINDOW FUNCTIONS
-- ================================================================================

-- Row number
SELECT
    first_name,
    last_name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;

-- Rank (same salary = same rank, gaps in ranking)
SELECT
    first_name,
    last_name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rnk
FROM employees;

-- Dense Rank (no gaps)
SELECT
    first_name,
    last_name,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rnk
FROM employees;

-- Rank within department
SELECT
    first_name,
    last_name,
    dept_id,
    salary,
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dept_rank
FROM employees;

-- Running total
SELECT
    first_name,
    salary,
    SUM(salary) OVER (ORDER BY emp_id) AS running_total
FROM employees;

-- Department-wise running total
SELECT
    first_name,
    dept_id,
    salary,
    SUM(salary) OVER (PARTITION BY dept_id ORDER BY emp_id) AS dept_running_total
FROM employees;


-- ================================================================================
-- COMMON INTERVIEW QUERIES
-- ================================================================================

-- 1. Second highest salary
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Alternative using LIMIT
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- 2. Nth highest salary (N = 3 in this example)
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;  -- N-1

-- 3. Find duplicate emails (if any existed)
SELECT email, COUNT(*) as count
FROM employees
GROUP BY email
HAVING COUNT(*) > 1;

-- 4. Department with highest total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY total_salary DESC
LIMIT 1;

-- 5. Employees who earn more than their managers
SELECT
    e.first_name AS employee,
    e.salary AS emp_salary,
    m.first_name AS manager,
    m.salary AS mgr_salary
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;

-- 6. Top 2 earners per department
SELECT * FROM (
    SELECT
        first_name,
        last_name,
        dept_id,
        salary,
        DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
) ranked
WHERE rnk <= 2;

-- 7. Employees hired in last year
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

-- 8. Year-wise employee count
SELECT
    YEAR(hire_date) AS hire_year,
    COUNT(*) AS employees_hired
FROM employees
GROUP BY YEAR(hire_date)
ORDER BY hire_year;

-- 9. Cumulative salary by hire date
SELECT
    hire_date,
    first_name,
    salary,
    SUM(salary) OVER (ORDER BY hire_date) AS cumulative_salary
FROM employees
ORDER BY hire_date;

-- 10. Employees working on multiple projects
SELECT
    e.first_name,
    e.last_name,
    COUNT(ep.project_id) AS project_count
FROM employees e
JOIN employee_projects ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.first_name, e.last_name
HAVING COUNT(ep.project_id) > 1;


-- ================================================================================
-- VIEWS
-- ================================================================================

-- Create a view for employee details
CREATE VIEW employee_details AS
SELECT
    e.emp_id,
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    e.email,
    e.salary,
    d.dept_name,
    m.first_name AS manager_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- Use the view
SELECT * FROM employee_details WHERE salary > 70000;

-- Drop view
-- DROP VIEW employee_details;


-- ================================================================================
-- STORED PROCEDURE (Example)
-- ================================================================================

DELIMITER //

CREATE PROCEDURE GetEmployeesByDept(IN dept_name_param VARCHAR(50))
BEGIN
    SELECT e.first_name, e.last_name, e.salary, d.dept_name
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    WHERE d.dept_name = dept_name_param;
END //

DELIMITER ;

-- Call the procedure
-- CALL GetEmployeesByDept('Engineering');

-- Drop procedure
-- DROP PROCEDURE GetEmployeesByDept;


-- ================================================================================
-- CLEANUP (Optional)
-- ================================================================================

-- DROP TABLE employee_projects;
-- DROP TABLE projects;
-- DROP TABLE employees;
-- DROP TABLE departments;
-- DROP DATABASE company_db;
