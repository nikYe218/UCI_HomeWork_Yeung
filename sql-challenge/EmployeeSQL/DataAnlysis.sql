--1. List the following details of each employee: employee number, last name, first name, sex, and salary.

select
e.emp_no  "employee number",
e.last_name "last name",
e.first_name "first name",
e.sex,
s.salary
from employees e
join salaries s on e.emp_no=s.emp_no;


--2. List first name, last name, and hire date for employees who were hired in 1986.

select
e.first_name "first name",
e.last_name "last name",
e.hire_date "hire date"
--to_char(hire_date,'yyyy') "year"
from employees  e
where to_char(hire_date,'yyyy')='1986';


-- 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
select
d.dept_no "department number",
d.dept_name "department name",
m.emp_no "manager''s employee number",
e.last_name "last name",
e.first_name "first name"
from dept_manager m 
join employees e on m.emp_no=e.emp_no
join departments d on m.dept_no=d.dept_no;

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.
select
e.emp_no "employee number",
e.last_name "last name",
e.first_name "first name",
d.dept_name "department name"
from employees e 
join dept_emp de on e.emp_no=de.emp_no
join departments d on de.dept_no=d.dept_no;


--5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select
first_name "first name",
last_name "last name",
sex
from employees 
where upper(first_name)=upper('Hercules')
and upper(last_name) like 'B%';

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
select
e.emp_no "employee number",
e.last_name "last name",
e.first_name "first name",
d.dept_name "department name"
from employees e 
join dept_emp de on e.emp_no=de.emp_no
join departments d on de.dept_no=d.dept_no
where d.dept_name='Sales';


--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

select
e.emp_no "employee number",
e.last_name "last name",
e.first_name "first name",
d.dept_name "department name"
from employees e 
join dept_emp de on e.emp_no=de.emp_no
join departments d on de.dept_no=d.dept_no
where d.dept_name in ('Sales','Development');

--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

select
e.last_name, count(*) Freq_LastName
from employees e 
group by 
e.last_name
having count(*)>1
order by count(*) desc;