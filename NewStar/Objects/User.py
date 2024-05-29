class User:
    """
    用户类，表示系统中的不同用户角色及基本信息。

    Attributes:
        _user_id (int): 用户的唯一标识符，自动增长。
        _username (str): 用户的用户名。
        _password (str): 用户的密码。
        _role (str): 用户的角色，可选值为'admin', 'class_manager', 'student'。
        _class_id (int): 关联的班级ID，为外键。
        _student_id (int): 关联的学生ID，为外键且允许为空。

    Methods:
        get_user_id(): 获取用户ID。
        get_username(): 获取用户名。
        get_password(): 获取密码。
        get_role(): 获取用户角色。
        get_class_id(): 获取关联的班级ID。
        get_student_id(): 获取关联的学生ID。

        set_username(username): 设置用户名。
        set_password(password): 设置密码。
        set_role(role): 设置用户角色。
        set_class_id(class_id): 设置关联的班级ID。
        set_student_id(student_id): 设置关联的学生ID。
    """

    def __init__(self, id, username, password, role, class_id=None, student_id=None):
        self._user_id = id
        self._username = username
        self._password = password
        self._role = role
        self._class_id = class_id
        self._student_id = student_id

    def __init__(self, username, password, role, class_id=None, student_id=None):
        self._user_id = None
        self._username = username
        self._password = password
        self._role = role
        self._class_id = class_id
        self._student_id = student_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, id):
        self._user_id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        """设置用户名."""
        self._username = username

    @property
    def password(self):
        """返回密码."""
        return self._password

    @password.setter
    def password(self, password):
        """设置密码."""
        self._password = password

    @property
    def role(self):
        """返回用户角色."""
        return self._role

    @role.setter
    def role(self, role):
        """设置用户角色，包含有效性检查."""
        if role in ['admin', 'class_manager', 'student']:
            self._role = role
        else:
            raise ValueError("Invalid role. Role must be one of 'admin', 'class_manager', 'student'.")

    @property
    def class_id(self):
        """返回关联的班级ID."""
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        """设置关联的班级ID."""
        self._class_id = class_id

    @property
    def student_id(self):
        """返回关联的学生ID."""
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        """设置关联的学生ID，允许设为None."""
        self._student_id = student_id

    def __str__(self):
        """返回用户信息的字符串表示，便于打印和查看."""
        return (
            f"User Info:\n"
            f"\tUser ID: {self.user_id}\n"
            f"\tUsername: {self.username}\n"
            f"\tRole: {self.role}\n"
            f"\tClass ID: {self.class_id}\n"
            f"\t{self.student_id}"
        )

if __name__ == "__main__":
    u = User(1, "df", "fdz", 'admin')
    print(u)