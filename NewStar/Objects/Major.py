"""
:description: 实现专业类
:author: JavierChen
:version: 2.0
"""
class Major:
    """
        专业类，表示不同专业。

        Attributes:
            _major_id (int): 专业的唯一标识符。
            _major_name (str): 专业的名称。

        Methods:
            get_major_id(): 获取专业ID。
            set_major_id(id): 设置新的专业ID。
            get_major_name(): 获取专业名称。
            set_major_name(name): 设置新的专业名称。
        """
    def __init__(self, major_id, major_name):
        self._major_id = major_id
        self._major_name = major_name

    def __str__(self):
        return f"{self._major_name}专业的编号是{self._major_id}"

    @property
    def major_id(self):
        return self._major_id

    @major_id.setter
    def major_id(self, id):
        self._major_id = id

    @property
    def major_name(self):
        return self._major_name

    @major_name.setter
    def major_name(self, name):
        self._major_name = name

