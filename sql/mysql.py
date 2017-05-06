# Pakiet mysqlclient nie lubi sie z Python 3
# import MySQLdb
# import MySQLdb.cursors

# pymysql działa "od razu"
import pymysql
import pprint


# DictCursor
conn = pymysql.connect(host='localhost', user='root', passwd='****', db='northwind',
                       charset='utf8', cursorclass=pymysql.cursors.DictCursor)
sql = "select * from customers where city = %s"
city = 'New York'

try:
    with conn.cursor() as cursor:
        cursor.execute("insert into employees (first_name, last_name) values (%s, %s)", ('Łukasz', 'F'))
    conn.commit()

    with conn.cursor() as cursor:
        cursor.execute(sql, (city,))
        result = cursor.fetchall()
        pprint.pprint(result)

finally:
    conn.close()

# SSCursor
conn = pymysql.connect(host='localhost', user='root', passwd='****', db='northwind',
                       charset='utf8', cursorclass=pymysql.cursors.SSCursor)
try:
    with conn.cursor() as cursor:
        cursor.execute(sql, (city,))

        for row in cursor:
            print(row)
finally:
    conn.close()

# Właściwości kursora:
# cursor.callproc(procname, args) - wywolanie procedury składowanej
# cursor.nextset() - przemieszcza kursor do kolejnego zestawu wyników (ang. result set)
# cursor.fetchone() - pobiera jeden rekord
# cursor.fetchmany(n) - pobiera n rekordów
# cursor.fetchall() - pobiera wszystkie rekordy lub pozostałe rekordy jeśli wcześniej jakieś zostały pobrane

# Pobieranie wyniku zapytania
# mysql_store_result - pobiera wyniki z serwera na lokalną maszynę
# mysql_use_result - pozostawia wyniki zapytania na serwerze i daje możliwość pobierania ich jeden po drugim

# Rodzaje kursorow:
# Cursor - mysql_store_result, zwraca wiersze jako krotki
# DictCursor - mysql_store_result, zwraca wiersze jako słowniki, kluczem jest nazwa kolumny
# SSCursor - mysql_use_result, zwraca wiersze jako krotki
# SSDictCursor - mysql_use_result, zwraca wiersze jako słowniki, kluczem jest nazwa kolumny
