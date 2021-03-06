import sqlite3
import os

'''SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说
没有独立的维护进程，所有的维护都来自于程序本身。
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候
连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建
数据库文件，而是直接打开该数据库文件。
    连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库
    执行完任何操作后，都不需要提交事务的(commit)

    创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
    创建在内存上面： conn = sqlite3.connect('"memory:')

    下面我们一硬盘上面创建数据库文件为例来具体说明：
    conn = sqlite3.connect('c:\\test\\hongten.db')
    其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：

        commit()            --事务提交
        rollback()          --事务回滚
        close()             --关闭一个数据库链接
        cursor()            --创建一个游标

    cu = conn.cursor()
    这样我们就创建了一个游标对象：cu
    在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
    对于游标对象cu，具有以下具体操作：

        execute()           --执行一条sql语句
        executemany()       --执行多条sql语句
        close()             --游标关闭
        fetchone()          --从结果中取出一条记录
        fetchmany()         --从结果中取出多条记录
        fetchall()          --从结果中取出所有记录
        scroll()            --游标滚动

'''

#global var

#global var
#数据库文件绝句路径
DB_FILE_PATH = ''
#表名称
TABLE_NAME = ''
#是否打印sql
SHOW_SQL = True

def get_conn(path):
    conn = sqlite3.connect(path)  # type: sqlite3.Connection
    return conn

def get_cursor(conn: sqlite3.Connection): #-> sqlite3.Connection:
    return conn.cursor()

def drop_table(conn, table):
    '''如果表存在,则删除表，如果表中存在数据的时候，使用该
        方法的时候要慎用！'''
    if table is not None and table != '':
        sql = 'drop table if exists ' + table
        if SHOW_SQL:
            print('execute sql:[{}]'.format(table))
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print('the [{}] is empty!'.format(table))
    else:
        print('the [{}] is empty!'.format(table))

def create_table(conn, sql: str):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('execute sql: [{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('success create table !')
        close(cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def close(cu):
    '''
    :param cu:
    :return:
    '''
    if cu is not None:
        cu.close()
    '''
            try:
        if cu is not None:
            cu.close()
    finally:'''


def insert(conn, sql, data):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if data is not None:
            for d in data:
                if SHOW_SQL:
                    print('execute sql [{}], para [{}]'.format(sql, data))
                cu.execute(sql, d)
                conn.commit()
        close(cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def fetchall(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('execute sql: [{}]'.format(sql))
        cu.execute(sql)
        r = cu.fetchall()
        return r  # type: list
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def fetchone(conn, sql, data):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('execute sql: [{}], para [{}]'.format(sql, data))
        d = (data,)
        cu.execute(sql, d)
        r = cu.fetchall()
        return r  # type: list
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def update(conn, sql, data):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if data is not None:
            for d in data:
                if SHOW_SQL:
                    print('execute sql: [{}], para [{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
        close(cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def delete(conn, sql, data):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if data is not None:
            for d in data:
                if SHOW_SQL:
                    print('execute sql: [{}], para [{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
        close(cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

'''
def fetchall(conn, sql):
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('execute sql: [{}]'.format(sql))
    else:
        print('the [{}] is empty or equal None!'.format(sql))
'''


###############################################################
####            测试操作     START
###############################################################
def drop_table_test():
    '''删除数据库表测试'''
    print('删除数据库表测试...')
    conn = get_conn(DB_FILE_PATH)
    drop_table(conn, TABLE_NAME)


def create_table_test():
    '''创建数据库表测试'''
    print('创建数据库表测试...')
    create_table_sql = '''CREATE TABLE if not exists student  (
                          id INTEGER PRIMARY KEY not null ,
                          name char(20) NOT NULL,
                          gender char(4) DEFAULT NULL,
                          age INT DEFAULT NULL,
                          address varchar(200) DEFAULT NULL,
                          phone varchar(20) DEFAULT NULL
                        )'''
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_table_sql)

def save_test():
    '''保存数据测试...'''
    print('保存数据测试...')
    save_sql = '''INSERT INTO student values (NULL,?, ?, ?, ?, ?)'''
    data = [('Hongten', '男', 20, '广东省广州市', '13423****62'),
            ('Tom', '男', 22, '美国旧金山', '15423****63'),
            ('Jake', '女', 18, '广东省广州市', '18823****87'),
            ('Cate', '女', 21, '广东省广州市', '14323****32')]
    conn = get_conn(DB_FILE_PATH)
    insert(conn, save_sql, data)

def fetchall_test():
    '''查询所有数据...'''
    print('查询所有数据...')
    fetchall_sql = '''SELECT * FROM student'''
    conn = get_conn(DB_FILE_PATH)
    rs = fetchall(conn, fetchall_sql)
    for r in rs:
        print(r)

def fetchone_test():
    '''查询一条数据...'''
    print('查询一条数据...')
    fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
    data = 1
    conn = get_conn(DB_FILE_PATH)
    rs = fetchone(conn, fetchone_sql, data)
    print(rs)

def update_test():
    '''更新数据...'''
    print('更新数据...')
    update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenBB', 2),
            ('HongtenCC', 3),
            ('HongtenDD', 4)]
    conn = get_conn(DB_FILE_PATH)
    update(conn, update_sql, data)


def delete_test():
    '''删除数据...'''
    print('删除数据...')
    delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    data = [('HongtenAA', 1),
            ('HongtenCC', 3)]
    conn = get_conn(DB_FILE_PATH)
    delete(conn, delete_sql, data)

def init():
    '''初始化方法'''
    #数据库文件绝句路径
    global DB_FILE_PATH
    DB_FILE_PATH = 'hongten.db'
    #数据库表名称
    global TABLE_NAME
    TABLE_NAME = 'student'
    #是否打印sql
    global SHOW_SQL
    SHOW_SQL = True
    print('show_sql : {}'.format(SHOW_SQL))
    # 创建数据库表student
    create_table_test()
    #如果存在数据库表，则删除表
    drop_table_test()
    #创建数据库表student
    create_table_test()
    #向数据库表中插入数据
    save_test()

def main():
    init()
    fetchall_test()
    print('#' * 50)
    fetchone_test()
    print('#' * 50)
    update_test()
    fetchall_test()
    print('#' * 50)
    delete_test()
    fetchall_test()
    close(get_conn())

if __name__ == '__main__':
    main()
