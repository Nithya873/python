# Write your MySQL query statement below
select name ,sum(Transactions.amount) as balance
from Users
join Transactions
on Users.account=Transactions.account
group by Transactions.account
having sum(Transactions.amount)>10000