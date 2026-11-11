SELECT Department,ROUND(AVG(MonthlyIncome), 2) AS Average_Income
FROM employee_attrition
GROUP BY Department
ORDER BY Average_Income DESC;

