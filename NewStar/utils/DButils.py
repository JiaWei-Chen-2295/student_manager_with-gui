"""
:description: 数据库连接工具类
:author: JavierChen
:version: 1.0
"""
import yaml
import mysql.connector
from errno import errorcode
class DButils:
    @classmethod
    def get_DB_info(cls):
        """读取数据库配置"""
        config = {}
        with open('../../test_config/DBconnInfo.yml', 'r') as file:
            config = yaml.safe_load(file)
        return config

    @staticmethod
    def getConnction():
        conn = None
        config = DButils.get_DB_info()
        try:
            conn = mysql.connector.connect(user=config['username'], password=config['password'],
                                          host=config['host'],
                                          database=config['database'])
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        return conn

    @staticmethod
    def closeAll(conn, cursor):
        if conn != None:
            conn.close()
        if cursor != None:
            cursor.close()

if __name__ == '__main__':
    print(DButils.getConnction())
    conn = DButils.getConnction()
    DButils.closeAll(conn)