# Выведите поступления денег от пользователя с email 'vasya@mail.com'.
# В результат включите все столбцы таблицы и не меняйте порядка их вывода.

use billing_simple;

SELECT 
    *
FROM
    billing
WHERE
    payer_email = 'vasya@mail.com';
