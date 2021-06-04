# -*- coding: utf-8 -*-
# [Python操作MySQL]银行转账实例-代码流程(mysql数据库)
import pymysql,sys

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfer(self,source_acctid,target_acctid,money):
       try:
            #检查账号是否可用
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            #检查付款人是否有足够的钱
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
       except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, acctid):
        try:
            cursor = self.conn.cursor()
            sql = "select * from account where acctid = %s"%acctid
            cursor.execute(sql)
            print("check_acct_available:"+ sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s不存在" % acctid)
        finally:
            cursor.close()

    def has_enough_money(self, acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "select * from account where acctid = %s and money > %s" % (acctid, money)
            cursor.execute(sql)
            print("has_enough_money:"+ sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s没有足够的钱" % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "update account set money=money-%s where acctid = %s" % (money, acctid)
            cursor.execute(sql)
            print("reduce_money:"+ sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("账号%s减款失败" % acctid)
        finally:
            cursor.close()


    def add_money(self, acctid, money):
        try:
            cursor = self.conn.cursor()
            sql = "update account set money=money+%s where acctid = %s" % (money, acctid)
            cursor.execute(sql)
            print("add_money:"+ sql)
            rs = cursor.fetchall()
            if cursor.rowcount != 1:
                raise Exception("账号%s加款失败" % acctid)
        finally:
            cursor.close()

if __name__ == "__main__":
    source_acctid = sys.argv[1]     #源账户
    target_acctid = sys.argv[2]     #目标账户
    money = sys.argv[3]             #转账金额

    conn = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='314159',
        db='imooc',
        charset='utf8'
    )
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print("出现问题：" + str(e))
    finally:
        conn.close()
