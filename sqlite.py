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

    def table_main(self, tableformat: str = "api",  dbname: str = "test.db"):
        """
        create table using the connection and create atble
        :param dbname: name of the database where to create table
        :return:
        """
        database = dbname
        if tableformat == "web":
            sql_create_test_table = """ CREATE TABLE IF NOT EXISTS compdetailweb (
                                            stock_id text,
                                            corp_code text,
                                            corp_name,
                                            per text,
                                            twMper text,
                                            업종per text,
                                            pbr text,
                                            배당수익률 text
                                            ); """
        elif tableformat == "api":
            # add PIMARY KEY to have it be a unique identifier
            sql_create_test_table = """CREATE TABLE IF NOT EXISTS compdetailapi (
                                            stock_code text,
                                            fs_div text,
                                            rcept_no text,
                                            reprt_code text,
                                            bsns_year text,
                                            corp_code text,
                                            sj_div text,
                                            sj_nm text,
                                            account_id text,
                                            account_nm text,
                                            account_detail text,
                                            thstrm_nm text,
                                            thstrm_amount text,
                                            frmtrm_nm text,
                                            frmtrm_amount text,
                                            bfefrmtrm_nm text,
                                            bfefrmtrm_amount text,
                                            ord text
                                            ); """

        conn = self.create_connection(database)
        if conn is not None:
            self.create_table(conn, sql_create_test_table)
        else:
            print("error")

    def insert_row_format(self, conn, detail, tableformat: str = 'api'):
        """
        insert a specific table to the database
        :param conn:
        :param detail:
        :return:
        """
        if tableformat == "web":
            sql = """ INSERT INTO compdetailweb(stock_id,
                                            comp_id,
                                            name,
                                            per,
                                            twMper,
                                            업종per,
                                            pbr,
                                            배당수익률
                                            ) VALUES(?,?,?,?,?,?,?) """
        elif tableformat == "api":
            sql = """INSERT INTO compdetailapi (
                                            stock_code,
                                            fs_div,
                                            rcept_no,
                                            reprt_code,
                                            bsns_year,
                                            corp_code,
                                            sj_div,
                                            sj_nm,
                                            account_id,
                                            account_nm,
                                            account_detail,
                                            thstrm_nm,
                                            thstrm_amount,
                                            frmtrm_nm,
                                            frmtrm_amount,
                                            bfefrmtrm_nm,
                                            bfefrmtrm_amount,
                                            ord
                                            ) VALUEs(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """

        # sql = """INSERT INTO compdetailtop(comp_id, name, per, twMper, 업종per, pbr, 배당수익률) VALUES(?,?,?,?,?,?,?)"""
        cur = conn.cursor()
        cur.execute(sql, detail)
        return cur.lastrowid

    def insert_row(self, comp_data, table_format: str = "api"):
        database = "test.db"
        conn = self.create_connection(database)
        with conn:
            comp = comp_data
            row_id = self.insert_row_format(conn, comp, table_format)
            # print(row_id)


if __name__ == '__main__':
    a = SqlDB()
    a.table_main()
