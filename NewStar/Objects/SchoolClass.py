class SchoolClass:
    __class_id = 0
    __class_name = None
    __major_id = 0

    def __init__(self, id, name, mid):
        self.__class_id = id
        self.__class_name = name
        self.__major_id = mid
    def __str__(self):
        return f"{self.__class_name}班的编号是{self.__class_id}，专业代号是{self.__major_id}"