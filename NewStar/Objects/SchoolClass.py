"""
:description: 实现班级类
:author: JavierChen
:version: 2.0
"""
class SchoolClass:
    """
    班级类，用于存储和管理学校的班级信息，包括班级的唯一标识符、班级名称及对应的专业ID。

    Attributes:
        _class_id (int): 班级的唯一编号。
        _class_name (str): 班级的名称。
        _major_id (int): 班级所属专业的ID，与专业类(Major)关联。

    Methods:
        __str__(): 返回班级信息的字符串表示。
        class_id: 属性，用于获取/设置班级ID。
        class_name: 属性，用于获取/设置班级名称。
        major_id: 属性，用于获取/设置专业ID。
    """
    def __init__(self, class_name, major_id, class_id = None):
        self._class_id = class_id
        self._class_name = class_name
        self._major_id = major_id

    def __str__(self):
        return f"{self._class_name}班的编号是{self._class_id}，专业代号是{self._major_id}"

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, id):
        self._class_id = id

    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, name):
        self._class_name = name

    @property
    def major_id(self):
        return self._major_id

    @major_id.setter
    def major_id(self, mid):
        self._major_id = mid