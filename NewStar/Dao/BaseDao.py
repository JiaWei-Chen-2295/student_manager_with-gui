"""
:description: 数据库操作封装的父类
:author: JavierChen
:version: 1.0
"""
import mysql
from mysql.connector.abstracts import MySQLCursorAbstract

from NewStar.utils import DButils
class BaseDao:
    """
        操作数据库的基类
        实现基本的增删改
        因为 Python 没有类似 Java 的反射机制 故不实现查

        Methods:
            executeUpdate: 运行增删改的 sql 语句
        """
    def __init__(self):
        pass

    def executeUpdate(self, sql, *args):
        conn = None
        cursor = None

        try:
            conn = DButils.DButils.getConnction()
            cursor = conn.cursor(prepared=True)
            cursor.execute(sql, args)
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Error occurred: {err}")
            conn.rollback()
            return -1
        finally:
            DButils.DButils.closeAll(conn, None)

if __name__ == '__main__':
    dao = BaseDao()
    r = dao.executeUpdate("INSERT INTO Users (username, password, role, class_id, student_id) VALUES (?,?,?,?,?)",
                      '李梓阳',
                      'adminpass',
                      'admin',
                      None,
                      None
                      )
    if r != -1:
        print("success")





