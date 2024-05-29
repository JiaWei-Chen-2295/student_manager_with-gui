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
        """
                向 `Majors` 表插入一条新的专业记录。

                参数:
                    - major: `Major` 类的实例，包含要插入的专业名称 (`major_name`)。

                异常:
                    - 抛出异常，当插入操作失败时。
                """
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
        """
                根据专业ID更新 `Majors` 表中指定的专业记录。

                参数:
                    - major: `Major` 类的实例，需包含专业ID (`major_id`) 和新的专业名称 (`major_name`)。

                异常:
                    - 抛出异常，当更新操作失败时。
                """
        sql = "DELETE FROM Majors WHERE major_id = ?"
        r = BaseDao.executeUpdate(sql, Major.major_id)
        if r == -1:
            raise Exception

    def selectById(self, id):
        """
                根据专业ID从 `Majors` 表中删除指定的专业记录。

                参数:
                    - major: `Major` 类的实例，至少需要包含专业ID (`major_id`)。

                异常:
                    - 抛出异常，当删除操作失败时。
                """
        md = MajorDao()
        rs = md.selectAll()
        for _ in rs:
            if _.major_id == id:
                return _

    def selectAll(self):
        """
                根据专业ID查询 `Majors` 表中对应的记录。

                参数:
                    - id: 要查询的专业ID。

                返回:
                    - 查询到的 `Major` 实例，如果未找到，则应适当处理（当前示例未给出错误处理）。
                """
        major_list = []
        sql = f"SELECT * FROM Majors"
        bb = BaseDao()
        rs = bb.executeQuery(sql)
        for _ in rs:
            major = Major(_[1], _[0])
            major_list.append(major)
        return major_list

if __name__ == '__main__':
    md = MajorDao()
    rs = md.selectById(2)
    print(rs)
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

