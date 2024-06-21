# 2. Создайте базу данных SQLite. В ней две таблицы.
# В первой таблице 3 колонки, во второй 5.
# В каждую из таблиц добавить по три записи.

import sqlite3

connection = sqlite3.Connection('SQLite1.db')
cursor = connection.cursor()

cursor.execute('create table Table1 (id int, name text, surname text)')
cursor.execute('create table Table2 (id int, name text, surname text, dateofbirth text, Placeofbirth text)')

cursor.execute('insert into Table1 (id, name, surname) values (1002, "Ivan", "Sidorov")')
cursor.execute('insert into Table1 (id, name, surname) values (1003, "Serhei", "Ivanov")')
cursor.execute('insert into Table1 (id, name, surname) values (1001, "Dzmiyry", "Sokolov")')

# cursor.execute('delete from Table1 where id < 4')

cursor.execute('insert into Table2 (id, name, surname, dateofbirth, Placeofbirth) values (1002, "Ivan", "Sidorov", "13.12.1996", "г.Борисов")')
cursor.execute('insert into Table2 (id, name, surname, dateofbirth, Placeofbirth) values (1003, "Serhei", "Ivanov", "01.07.2006", "г.Борисов")')
cursor.execute('insert into Table2 (id, name, surname, dateofbirth, Placeofbirth) values (1003, "Dzmiyry", "Sokolov", "31.08.1989", "г.Борисов")')

connection.commit()
cursor.close()