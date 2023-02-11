--1
SELECT COUNT(distinct(JOB_ID)) as COUNT_JOB FROM employees;
--2
SELECT  avg(SALARY) as SALARY_AVG, COUNT(EMPLOYEE_ID) as EMPLOYEE_COUNT FROM employees where DEPARTMENT_ID=90;
--3
SELECT JOB_ID,COUNT(EMPLOYEE_ID) as EMPLOYEE_COUNT FROM employees GROUP BY JOB_ID;
--4
SELECT employees.FIRST_NAME, employees.LAST_NAME, employees.DEPARTMENT_ID, departments.DEPARTMENT_NAME FROM employees
left join departments on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID;
--5
SELECT first_name, last_name, job_id, department_id
FROM employees
JOIN departments USING (department_id)
JOIN locations USING (location_id)
WHERE city = 'London';