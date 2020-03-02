import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_aql):
    try:
        c = conn.cursor()
        c.execute(create_table_aql)
    except Error as e:
        print(e)

def main():
    database = "test.db"
    sql_create_test_table = """ CREATE TABLE IF NOT EXISTS compdetail (
                                    compid text,
                                    name text,
                                    per text,
                                    twMper text,
                                    업종per text,
                                    pbr text,
                                    배당수익률 text
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_test_table)
    else:
        print("error")

def insert_compdetail(conn, detail):
    sql = """INSERT INTO compdetail(compid, name, per, twMper, 업종per, pbr, 배당수익률) VALUES(?,?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, detail)
    return cur.lastrowid

def main2():
    database = "test.db"
    conn = create_connection(database)
    with conn:
        comp = ('123123', '삼선', '19.01', '15.97', '7.19', '1.80', '0.87%');
        compdetail_id = insert_compdetail(conn, comp)


if __name__ == '__main__':
    main()
    for i in range(100000):
        main2()
