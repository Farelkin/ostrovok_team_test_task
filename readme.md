<h1>Задача 1: Что может быть проще SQL?</h1>
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
    
<h3>Инструкция как пользоваться программой:</h3>
Перед запуском необходимо убедится, что файл "secrets.json" находится в той же 
директории, что и исполняемый файл

<h1>Задача 2: Smashing Wallpaper Downloader</h1>

Есть прекрасный сайт Smashing Magazine, который каждый месяц выкладывает
отличные обои для десктопа. Заходить каждый месяц и проверять, что там нового
дело не благородное, поэтому давайте попробуем автоматизировать эту задачу.
Требуется написать cli утилиту, которая будет качать все обои в требуемом
разрешение за указанный месяц-год в текущую директорию пользователя.
Вот тут находятся все обои, а здесь находятся обои за май 2017.

<h3>Инструкция как пользоваться программой:</h3>
Программа работает на OS Linux. Для её запуска используйте команду:
"Python3 ex2.py"

Примеры ввода:
run
09-2015
640x480


