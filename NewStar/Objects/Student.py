"""
:description: 实现学生（Student）类，用于存储和管理学生个人信息，包括学号、姓名、一卡通号及所在班级ID。
:author: JavierChen
:version: 2.0

此类封装了学生的基本属性，并提供了相关的方法来获取和设置这些属性值，同时包含一个方法用于展示学生的详细信息。
"""

class Student:
    """
    学生类，代表学校中的一个学生实体，记录其学号、姓名、一卡通号及归属的班级信息。

    Attributes:
        _id (int): 学生的唯一学号。
        _name (str): 学生的姓名。
        _card_num (str): 学生的一卡通号码。
        _class_id (int): 学生所在班级的ID，与班级类(SchoolClass)关联。

    Methods:
        __init__(): 初始化学生实例。
        __str__(): 返回学生详细信息的字符串表示。
        get_id(): 获取学生学号。
        set_id(id): 设置学生的新学号。
        get_name(): 获取学生姓名。
        set_name(name): 设置学生的新姓名。
        get_card_num(): 获取学生一卡通号。
        set_card_num(card_num): 设置学生新的一卡通号。
        get_class_id(): 获取学生所在班级ID。
        set_class_id(class_id): 设置学生新的班级ID。
    """

    def __init__(self, id, name, card_num, class_id):
        self._id = id
        self._name = name
        self._card_num = card_num
        self._class_id = class_id

    @property
    def id(self):
        """学号"""
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def card_num(self):
        return self._card_num

    @card_num.setter
    def card_num(self, card_num):
        self._card_num = card_num

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        self._class_id = class_id

    def __str__(self):
        return f"学生信息：\n学号：{self.id}\n姓名：{self.name}\n一卡通号：{self.card_num}\n所在班级ID：{self.class_id}"

if __name__ == "__main__":
    pass
