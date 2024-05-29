"""
:description: 操作数据库中 Students 表的类
:author: JavierChen
:version: 1.0
"""
from NewStar.Dao.BaseDao import BaseDao
from NewStar.Objects.Student import Student


class StudentDao():
    """
    数据库 Students 表操作类，用于管理 Students 表中的学生记录。

    Methods:
        insert: 向 Students 表插入一个新的学生记录。
        update: 根据学生ID更新 Students 表中已有学生记录。
        delete: 根据学生ID从 Students 表中删除学生记录。
        selectById: 根据学生ID查询 Students 表中的学生记录。
        selectAll: 查询 Students 表中的所有学生记录。
    """

    def insert(self, student):
        """
        向 Students 表插入一条新的学生记录。

        参数:
            - student: `Student` 类的实例，包含学生的学号、姓名、一卡通号及班级ID。

        异常:
            - 抛出异常，当插入操作失败时。
        """
        sql = "INSERT INTO Students (student_name, student_card_num, class_id) VALUES (?, ?, ?)"
        r = BaseDao.executeUpdate(sql, student.name, student.card_num, student.class_id)
        if r == -1:
            raise Exception("Insert operation failed.")

    def update(self, student):
        """
        根据学生ID更新 Students 表中已有的学生记录。

        参数:
            - student: `Student` 类的实例，需包含学生ID及要更新的其他信息。

        异常:
            - 抛出异常，当更新操作失败时。
        """
        sql = "UPDATE Students SET student_name = ?, student_card_num = ?, class_id = ? WHERE student_id = ?"
        r = BaseDao.executeUpdate(sql, student.name, student.card_num, student.class_id, student.id)
        if r == -1:
            raise Exception("Update operation failed.")

    def drop(self, student):
        """
        根据学生ID从 Students 表中删除学生记录。

        参数:
            - student: `Student` 类的实例，至少需要包含学生ID。

        异常:
            - 抛出异常，当删除操作失败时。
        """
        sql = "DELETE FROM Students WHERE student_id = ?"
        r = BaseDao.executeUpdate(sql, student.id)
        if r == -1:
            raise Exception("Delete operation failed.")

    def selectById(self, id):
        """
        根据学生ID查询 Students 表中的学生记录。

        参数:
            - id: 要查询的学生ID。

        返回:
            - 查询到的 `Student` 实例，如果没有找到则返回 None 或抛出异常（根据需求选择实现）。
        """
        sd = StudentDao()
        rs = sd.selectAll()
        for _ in rs:
            if _.id == id:
                return _

    def selectAll(self):
        """
        查询 Students 表中的所有学生记录。

        返回:
            - 包含所有学生记录的 `Student` 实例列表。
        """
        student_list = []
        sql = "SELECT * FROM Students"
        bd = BaseDao()
        rs = bd.executeQuery(sql)
        for row in rs:
            student = Student(row[1], row[2], row[3], row[0])
            student_list.append(student)
        return student_list

if __name__ == '__main__':
    m = Student("fht4", 222222222222221166, 2, 7)
    md = StudentDao()
    md.drop(m)
    # 示例代码可以在这里编写，用于测试 StudentDao 类的各种方法
    # md = StudentDao()
    # rs = md.selectById(2)
    # print(rs)

    # m = Student("fht4", 222222222222221166, 2)
    # md = StudentDao()
    # md.insert(m)
    #

    #
