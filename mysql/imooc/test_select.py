# -*- coding: utf-8 -*-
# Python实例演示select数据(mysql数据库)
import pymysql

conn = pymysql.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '314159',
    db = 'imooc',
    charset = 'utf8'
)

cursor = conn.cursor()

sql = "select * from user"
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
    print ("userid=%s, username=%s" % row)

cursor.close()
conn.close()
