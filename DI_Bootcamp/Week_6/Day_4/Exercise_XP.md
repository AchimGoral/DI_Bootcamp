Basic Select Statement:

1.
select first_name as "First Name",last_name as "Last Name"
from employees

2.
select department_id
from employees
group by department_id
having count(department_id) = 1

3.
select first_name, last_name
from employees
order by first_name desc

4.
select first_name, last_name, salary, salary*0.15 as "PF"
from employees

5.
select employee_id, first_name, last_name, salary
from employees
order by salary asc

6.
select sum(salary)
from employees

7.
select min(salary), max(salary)
from employees

8.
select avg(salary)
from employees

9.
select count(employee_id)
from employees

10.
select upper(first_name)
from employees

11.
select left(first_name, 3)
from employees

12.
select CONCAT(first_name, ' ', last_name) 
as "Full Name"
from employees

13.
select first_name, last_name, 
(length(first_name) + length (last_name)) as "Length Full Name"
from employees

-- or

select first_name, last_name, length(CONCAT(first_name, last_name)) 
as "Full Name"
from employees

14.
select * from employees where first_name ~ '\d'

15.
select *
from employees
limit 10

Restricting And Sorting

1.
select first_name, last_name, salary
from employees
where salary between '10000' and '15000'

2.
select first_name, last_name, hire_date
from employees
where hire_date between '01/01/1987' and '31/12/1987'

3.
select first_name, last_name
from employees
where first_name like '%c%' 
and first_name like '%e%'

4.
select first_name, last_name, job_title, salary
from employees
join jobs
on employees.job_id = jobs.job_id
where job_title not in ('Programmer', 'Shipping Clerk')
and salary not in ('4500', '10000', '15000')

5.
select last_name
from employees
where length(last_name) = 6

6.
select last_name
from employees
where position('e' in last_name) = 3

7.
select distinct job_title
from employees
join jobs
on employees.job_id = jobs.job_id

8.
select *
from employees
where upper(last_name) in ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD')

Update Statement

1.

2.
update employees
set email = 'available'
from departments
where employees.department_id = departments.department_id
and departments.department_name = 'Accounting'

3.
update employees
set salary = 8000
where employee_id = 105
and salary < 5000

4.
update employees set salary=(salary*.25)
where department_id=4;  
update employees set salary=(salary*.15)
where department_id=9;
update employees set salary=(salary*.1)
where department_id=11