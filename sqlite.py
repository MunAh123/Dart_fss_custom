import sqlite3
from sqlite3 import Error


class SqlDB(object):
    def __init__(self):
        self.cur_conn = ""

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
            return e

        return conn

    def create_table(self, conn, create_table_aql):
        try:
            c = conn.cursor()
            c.execute(create_table_aql)
        except Error as e:
            print(e)

    def table_main(self):
        database = "test.db"
        sql_create_test_table = """ CREATE TABLE IF NOT EXISTS compdetailtop (
                                        compid text,
                                        name text,
                                        per text,
                                        twMper text,
                                        업종per text,
                                        pbr text,
                                        배당수익률 text
                                        ); """

        conn = self.create_connection(database)

        if conn is not None:
            self.create_table(conn, sql_create_test_table)
        else:
            print("error")

    def insert_compdetailtop(self, conn, detail):
        sql = """INSERT INTO compdetailtop(compid, name, per, twMper, 업종per, pbr, 배당수익률) VALUES(?,?,?,?,?,?,?)"""
        cur = conn.cursor()
        cur.execute(sql, detail)
        return cur.lastrowid

    def compdetailtop_insert_main(self, comp_data):
        database = "test.db"
        conn = self.create_connection(database)
        with conn:
            comp = comp_data
            compdetail_id = self.insert_compdetail_top(conn, comp)


if __name__ == '__main__':
    print("A")
