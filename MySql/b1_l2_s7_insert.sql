# Добавьте в таблицу одну запись о платеже со следующими значениями:
# email плательщика: 'pasha@mail.com'
# email получателя: 'katya@mail.com'
# сумма: 300.00
# валюта: 'EUR'
# дата операции: 14.02.2016
# комментарий: 'Valentines day present)' 

use billing_simple;

INSERT INTO billing(
	payer_email, 
    recipient_email, 
    sum, 
    currency, 
    billing_date, 
    comment)
values (
'pasha@mail.com',
'katya@mail.com',
'300.00',
'EUR',
'2016-02-14',
'Valentines day present)')
