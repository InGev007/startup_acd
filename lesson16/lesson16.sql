select * from employees order by FIRST_NAME;
select FIRST_NAME,LAST_NAME,SALARY,SALARY*0.15 as TAX from employees;
select sum(SALARY) as SALARY_SUM from employees;
select max(salary) as SALARY_MAX, min(salary) as SALARY_MIN from employees;
select avg(SALARY) as SALARY_AVG, count(EMPLOYEE_ID) as EMPLOYEE_COUNT from employees;