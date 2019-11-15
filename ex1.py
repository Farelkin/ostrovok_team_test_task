import psycopg2
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

conn = psycopg2.connect(host="151.248.122.170",
                        database="ostrovok",
                        user="admin_ostrova",
                        password="ostrovok")
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
