# Write your MySQL query statement below
select Users.name as NAME,sum(Transactions.amount)  as BALANCE
from Users
join Transactions
on Users.account=Transactions.account
GROUP BY Users.name
having BALANCE>10000