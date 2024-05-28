class Major:
    __major_id = 0
    __major_name = None

    def __init__(self, id, name):
        self.__major_id = id
        self.__major_name = name
    def __str__(self):
        return f"{self.__major_name}专业的编号是{self.__major_id}"
    def getId(self):
        return self.__major_id
    def getName(self):
        return self.__major_name
    def setId(self, id):
        self.__major_id = id
    def setName(self, name):
        self.__major_name = name