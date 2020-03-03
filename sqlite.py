import sqlite3
from sqlite3 import Error


class SqlDB(object):
    def __init__(self):
        self.cur_conn = ""

    def create_connection(self, db_file: str = "test.db"):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
            return e
        return conn

    def create_table(self, conn, create_table_aql):
        """
        :param conn: connection
        :param create_table_aql: table format
        :return:
        should only need to be used within table main
        """
        try:
            c = conn.cursor()
            c.execute(create_table_aql)
        except Error as e:
            print(e)

    def table_main(self, dbname: str = "test.db"):
        """
        create table using the connection and create atble
        :param dbname: name of the database where to create table
        :return:
        """
        database = dbname
        sql_create_test_table = """ CREATE TABLE IF NOT EXISTS compdetailtop (
                                        comp_id text,
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

    def insert_row_format(self, conn, detail):
        """
        insert a specific table to the database
        :param conn:
        :param detail:
        :return:
        """
        sql = """INSERT INTO compdetailtop(comp_id, name, per, twMper, 업종per, pbr, 배당수익률) VALUES(?,?,?,?,?,?,?)"""
        cur = conn.cursor()
        cur.execute(sql, detail)
        return cur.lastrowid

    def insert_row(self, comp_data):
        database = "test.db"
        conn = self.create_connection(database)
        with conn:
            comp = comp_data
            row_id = self.insert_row_format(conn, comp)
            print(row_id)


if __name__ == '__main__':
    print("A")
