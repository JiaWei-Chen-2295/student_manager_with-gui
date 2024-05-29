"""
:description: 操作数据库中 Majors 表的类
:author: JavierChen
:version: 1.0
"""
from NewStar.Dao.BaseDao import BaseDao
from NewStar.Objects.Major import Major


class MajorDao():
    """
        数据库 Majors 表操作类，用来修改 Majors 表。

        Attributes:

        Methods:
            insert: 增加专业于数据库。
            update: 修改已有的条目，以 id 为参数。
            drop: 根据 id 删除数据库表的一条数据。
            selectById: 根据 id 查询表的条目
            selectAll: 查询所有数据
        """

    def insert(self, Major):
        sql = "INSERT INTO Majors (major_name) VALUES (?)"
        r = BaseDao.executeUpdate(sql, Major.major_name)
        if r == -1:
            raise Exception

    def update(self, Major):
        sql = "UPDATE Majors SET major_name = ? WHERE major_id = ?"
        r = BaseDao.executeUpdate(sql, Major.major_name, Major.major_id)
        if r == -1:
            raise Exception

    def drop(self, Major):
        sql = "DELETE FROM Majors WHERE major_id = ?"
        r = BaseDao.executeUpdate(sql, Major.major_id)
        if r == -1:
            raise Exception

    def selectById(self, id):
        sql = "SELECT * FROM Majors WHERE magor_id = ?"
        rs = BaseDao.executeQuery(sql, id)
        return rs
if __name__ == '__main__':
    """
    m = Major("物联网工程")
    md = MajorDao()
    md.insert(m)
    """

    """
    m = Major("物联网工程", 4)
    md = MajorDao()
    md.update(m)

    m = Major("物联网工程", 4)
    md = MajorDao()
   
    md.drop(m)
"""
    md = MajorDao()
    print(md.selectById(4))
