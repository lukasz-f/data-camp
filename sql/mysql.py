#pakiet mysqlclient nie lubi sie z Python 3
#import MySQLdb
#import MySQLdb.cursors

import pymysql
import pprint

# mysql_store_result (Cursor) vs mysql_use_result (SSCursor)
# rodzaje kursorow Cursor, DictCursor, SSCursor, SSDictCursor

# DictCursor
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='northwind',
                       charset='utf8', cursorclass=pymysql.cursors.DictCursor)
sql = "select * from customers where city = %s"
city = 'New York'

try:
    with conn.cursor() as cursor:
        cursor.execute("insert into employees (first_name, last_name) values (%s, %s)", ('Łukasz', 'Frankiewicz'))
    conn.commit()

    with conn.cursor() as cursor:
        cursor.execute(sql, (city,))

        # fetchall, fetchone
        result = cursor.fetchall()
        pprint.pprint(result)

finally:
    conn.close()

# SSCursor
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='northwind',
                       charset='utf8', cursorclass=pymysql.cursors.SSCursor)
try:
    with conn.cursor() as cursor:
        cursor.execute(sql, (city,))

        for row in cursor:
            print(row)
finally:
    conn.close()
