#!/usr/bin/env python3

import MySQLdb

def main_sql(database_address, user, passwd , warehouse ,command):
    db = MySQLdb.connect(database_address, user,
                         passwd, warehouse, charset='utf8')
    cursor = db.cursor()
    cursor.execute(command)
    data_sql = cursor.fetchone()
    print(data_sql)

if __name__ == '__main__':
    main_sql(database_address='数据库地址',
        user='数据库用户名', passwd='数据库密码' , warehouse='数据库库名' ,command='执行sql语句')