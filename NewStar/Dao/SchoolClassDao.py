"""
:description: 操作数据库中 Classes 表的类
:author: JavierChen
:version: 1.0
"""
from NewStar.Dao.BaseDao import BaseDao
from NewStar.Objects.SchoolClass import SchoolClass


class SchoolClassDao():
    """
        数据库 classes 表操作类

        Attributes:

        Methods:
            insert: 增加班级于数据库。
            update: 修改已有的条目，以 id 为参数。
            drop: 根据 id 删除数据库表的一条数据。
            selectById: 根据 id 查询表的条目
            selectAll: 查询所有数据
        """

    def insert(self, SchoolClass):
        """
                向 `Classes` 表插入一条新的班级记录。

                参数:
                    - school_class: `SchoolClass` 实例，包含班级名称和所属专业ID。

                异常:
                    - 插入失败时抛出异常。
                """
        sql = "INSERT INTO Classes (class_name, major_id) VALUES (?,?)"
        r = BaseDao.executeUpdate(sql,  SchoolClass.class_name, SchoolClass.major_id)
        if r == -1:
            raise Exception

    def update(self, SchoolClass):
        """
            - **Description**: 根据班级ID更新 `Classes` 表中的班级信息。
          - **Parameters**:
            - `school_class`: `SchoolClass` 实例，需包含班级ID (`class_id`)、班级名称 (`class_name`) 及所属专业ID (`major_id`)。
          - **Raises**: 更新操作失败时抛出异常。

        """
        sql = "UPDATE Classes SET class_name = ?,major_id = ? WHERE class_id = ?"
        r = BaseDao.executeUpdate(sql, SchoolClass.class_name, SchoolClass.major_id, SchoolClass.class_id)
        if r == -1:
            raise Exception

    def drop(self, SchoolClass):
        """
            - **drop(SchoolClass school_class)**:
              - **Description**: 根据班级ID从 `Classes` 表中删除指定的班级记录。
              - **Parameters**:
                - `school_class`: `SchoolClass` 实例，至少包含班级ID (`class_id`)。
              - **Raises**: 删除操作失败时抛出异常。
        """
        sql = "DELETE FROM Classes WHERE class_id = ?"
        r = BaseDao.executeUpdate(sql, SchoolClass.class_id)
        if r == -1:
            raise Exception

    def selectById(self, id):
        """
                根据班级ID查询 `Classes` 表中的记录。

                参数:
                    - id: 班级ID。

                返回:
                    - 查询到的 `SchoolClass` 实例，如果没有找到则应适当处理。
                """
        scd = SchoolClassDao()
        rs = scd.selectAll()
        for _ in rs:
            if _.class_id == id:
                return _

    def selectAll(self):
        """
        - **selectAll()**:
      - **Description**: 查询 `Classes` 表中的所有班级记录。
      - **Returns**: 包含所有班级记录的 `SchoolClass` 实例列表。
        :return: 有 SchoolClass 对象的列表
        """

        class_list = []
        sql = f"SELECT * FROM Classes"
        bb = BaseDao()
        rs = bb.executeQuery(sql)
        for _ in rs:
            _class = SchoolClass(_[1], _[2], _[0])
            class_list.append(_class)
        return class_list


if __name__ == '__main__':
    pass
    # md = SchoolClassDao()
    # rs = md.selectById(2)
    # print(rs)

     # m = SchoolClass("计科3班", 2)
     # md = SchoolClassDao()
     # md.insert(m)
    #
    # m = SchoolClass("物联网工程", 1, 6)
    # md = SchoolClassDao()
    # md.update(m)
    #
    # m = SchoolClass("物联网工程", 1, 6)
    # md = SchoolClassDao()
    #
    # md.drop(m)


