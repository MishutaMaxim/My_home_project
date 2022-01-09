# Удалите из таблицы записи, где адрес плательщика или адрес получателя установлен в неопределенное значение или пустую строку.

use billing_simple;

DELETE FROM billing 
WHERE
    payer_email IS NULL OR payer_email = ''
    OR recipient_email IS NULL
    OR recipient_email = '';