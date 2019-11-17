import psycopg2
import os
import json
from pprint import pprint

"""
Задача 1: Что может быть проще SQL?
Вам дана таблица в postgres, которая представляет из себя список сотрудников с 
их зарплатами и отделами. Необходимо написать запрос, который будет выбирать 
человека с максимальной зарплатой из каждого отдела.
В качестве тестовых данных можете использовать дамп таблицы, пример схемы:

postgres=# \d employee
            Table "public.employee"
   Column   |         Type          | Modifiers
------------+-----------------------+-----------
 id         | integer               | not null
 name       | character varying(30) |
 department | character varying(30) |
 salary     | integer               |
Indexes:
    "employee_pkey" PRIMARY KEY, btree (id)
"""
BASE_DIR = os.path.abspath(os.curdir)

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        print('Secrets not downloaded')


conn = psycopg2.connect(host=get_secret('host'),
                        database=get_secret('database'),
                        user=get_secret('user'),
                        password=get_secret('password'))
cur = conn.cursor()
cur.execute('WITH table_1 AS '
            '(SELECT DISTINCT department, MAX(salary) as salary '
            'FROM employee '
            'GROUP BY department '
            'ORDER BY department)'
            ''
            'SELECT name '
            'FROM table_1, employee '
            'WHERE employee.salary = table_1.salary;')
max_salary = cur.fetchall()
pprint(max_salary)
cur.close()
