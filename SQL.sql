create database employee;
use employee;

create table employee (
emp_id INT PRIMARY KEY,
name VARCHAR(50),
gender VARCHAR(20),
department VARCHAR(30),
designation VARCHAR(20),
salary DECIMAL(10,2),
experience INT(2),
city VARCHAR(20),
joining_date date
);

INSERT INTO employee VALUES
(101,'Amit','Male','HR','Manager',65000,8,'Bangalore','2020-03-15'),
(102,'Priya','Female','IT','Developer',75000,6,'Mysore','2021-07-20'),
(103,'Rahul','Male','Finance','Accountant',55000,5,'Bangalore','2022-01-18'),
(104,'Sneha','Female','Sales','Sales Executive',48000,4,'Chennai','2023-05-10'),
(105,'Kiran','Male','IT','Developer',70000,7,'Hyderabad','2019-11-25'),
(106,'Divya','Female','HR','HR Executive',45000,3,'Bangalore','2024-02-15'),
(107,'Arjun','Male','Marketing','Executive',52000,6,'Delhi','2020-06-30'),
(108,'Pooja','Female','IT','Tester',60000,5,'Bangalore','2023-08-12'),
(109,'Manoj','Male','Finance','Manager',80000,10,'Mumbai','2018-09-05'),
(110,'Anjali','Female','Sales','Manager',68000,9,'Bangalore','2019-04-18'),
(111,'Ravi','Male','IT','Developer',72000,8,'Pune','2022-11-11'),
(112,'Neha','Female','Marketing','Executive',50000,4,'Mysore','2023-09-01'),
(113,'Suresh','Male','HR','Recruiter',43000,2,'Bangalore','2024-03-20'),
(114,'Meena','Female','Finance','Analyst',62000,6,'Chennai','2021-10-15'),
(115,'Ajay','Male','IT','Developer',78000,9,'Hyderabad','2018-07-19'),
(116,'Deepa','Female','Sales','Executive',47000,3,'Bangalore','2024-01-10'),
(117,'Vijay','Male','Marketing','Manager',85000,11,'Delhi','2017-05-12'),
(118,'Kavya','Female','IT','Tester',59000,5,'Mysore','2022-08-25'),
(119,'Naveen','Male','Finance','Accountant',54000,4,'Bangalore','2023-11-11'),
(120,'Shreya','Female','HR','Executive',46000,3,'Pune','2024-05-06'),
(121,'Harish','Male','Sales','Executive',51000,5,'Hyderabad','2022-04-20'),
(122,'Asha','Female','Marketing','Executive',53000,6,'Bangalore','2021-09-15'),
(123,'Rakesh','Male','IT','Developer',82000,12,'Chennai','2016-12-10'),
(124,'Nisha','Female','Finance','Manager',90000,13,'Mumbai','2015-06-05'),
(125,'Vinay','Male','HR','Manager',67000,8,'Bangalore','2020-02-18');

select *from employee;
select * from employee where salary > 500000;
select * from employee where city = 'Banglore';
select * from employee where experience > 5;
select MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary, AVG(salary) AS average_salary from employee;

select department, AVG(salary) AS average_salary from employee group by department;
select department, COUNT(*) AS employee_COUNT from employee group by department;
select * from employee order by salary desc limit 5;
select *  from employee where  joining_date > '2023-12-31';
select department, count(*) AS total_employee from employee group by department having count(*) > 5;

select *  from employee;