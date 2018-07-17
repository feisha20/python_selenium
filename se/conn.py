# -*- coding: UTF-8 -*-
import pymysql
import helper

# 数据库配置文件
conf_file = "DB.conf"


# 连接数据库
def get_con(db_name):
    host = helper.get_config_item(db_name, "host", f=conf_file)
    port = int(helper.get_config_item(db_name, "port", f=conf_file))
    user = helper.get_config_item(db_name, "user", f=conf_file)
    password = helper.get_config_item(db_name, "password", f=conf_file)
    db = helper.get_config_item(db_name, "db", f=conf_file)
    con = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
    return con


# 获取执行查询的对象
def get_cursor(db_name):
    con = get_con(db_name)
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    return cursor


# sql查询返回单条记录
def sql_select_one(db_name, sql):
    cursor = get_cursor(db_name)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


# sql查询返回多条记录
def sql_select_all(db_name, sql):
    cursor = get_cursor(db_name)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result