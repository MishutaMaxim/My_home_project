# Выведите в качестве результата одного запроса общее количество заказов, 
# сумму стоимостей (бюджетов) всех проектов, средний срок исполнения заказа в днях.


use project_simple;

SELECT 
    COUNT(project_name),
    SUM(budget),
    AVG(DATEDIFF(project_finish, project_start))
FROM
    project;