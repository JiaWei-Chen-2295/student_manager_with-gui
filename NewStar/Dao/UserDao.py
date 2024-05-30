"""
:description: 操作数据库中 User 表的类
:author: JavierChen
:version: 2.0
"""
from NewStar.Dao.BaseDao import BaseDao
from NewStar.Objects.User import User


class UserDao():
    """
        数据库 Users 表操作类，用于管理 Users 表中的用户记录。

        Methods:
            insert: 向 Users 表插入一个新的用户记录。
            update: 根据用户ID更新 Users 表中已有用户记录。
            delete: 根据用户ID从 Users 表中删除用户记录。
            selectById: 根据用户ID查询 Users 表中的用户记录。
            selectAll: 查询 Users 表中的所有用户记录。
    """

    def insert(self, User):
        """
                向 Users 表插入一条新的用户记录。

                参数:
                    - user: `User` 类的实例，包含用户的用户名、密码、角色、班级ID及学生ID。

                异常:
                    - 抛出异常，当插入操作失败时。
         """
        sql = "INSERT INTO Users (username, password, role, class_id, student_id) VALUES (?, ?, ?, ?, ?)"
        r = BaseDao.executeUpdate(sql, User.username, User.password, User.role, User.class_id, User.student_id)
        if r == -1:
            raise Exception("Insert operation failed.")

    def update(self, User):
        """
                根据用户ID更新 Users 表中已有的用户记录。

                参数:
                    - user: `User` 类的实例，需包含用户ID及要更新的其他信息。

                异常:
                    - 抛出异常，当更新操作失败时。
                """
        sql = f"UPDATE Users SET username = ?, password = ?, role = ?, class_id = ?, student_id = ? WHERE user_id = ?"
        r = BaseDao.executeUpdate(sql, User.username, User.password, User.role, User.class_id, User.student_id, User.user_id)
        if r == -1:
            raise Exception("Update operation failed.")

    def drop(self, User):
        """
                根据用户ID从 Users 表中删除用户记录。

                参数:
                    - user: `User` 类的实例，至少需要包含用户ID。

                异常:
                    - 抛出异常，当删除操作失败时。
        """
        sql = "DELETE FROM Users WHERE user_id = ?"
        r = BaseDao.executeUpdate(sql, User.user_id)
        if r == -1:
            raise Exception("Delete operation failed.")

    def selectById(self, id):
        """
        根据用户ID查询 Users 表中的用户记录。

        参数:
            - user_id: 要查询的用户ID。

        返回:
            - 查询到的 `User` 实例，如果没有找到则返回 None 或抛出异常（根据需求选择实现）。
        """
        ud = UserDao()
        rs = ud.selectAll()
        for _ in rs:
            if _.user_id == id:
                return _

    def selectAll(self):
        """
        查询 Users 表中的所有用户记录。

        返回:
            - 包含所有用户记录的 `User` 实例列表。
        """
        user_list = []
        sql = "SELECT * FROM Users"
        bd = BaseDao()
        rs = bd.executeQuery(sql)
        for row in rs:
            user = User(row[1], row[2], row[3], row[4], row[5], row[0])
            user_list.append(user)
        return user_list

if __name__ == '__main__':
    m = User(None,None,'admin',id=10)
    md = UserDao()
    md.drop(m)
    # 示例代码可以在这里编写，用于测试 StudentDao 类的各种方法
    # md = UserDao()
    # rs = md.selectById(2)
    # print(rs)

    # m = User("fht4", '2a1166', 'admin',1,1,9)
    # md = UserDao()
    # md.update(m)

