select count(distinct(JOB_ID)) from employees;
select  avg(SALARY) as SALARY_AVG, count(EMPLOYEE_ID) as EMPLOYEE_COUNT from employees where DEPARTMENT_ID=90;
