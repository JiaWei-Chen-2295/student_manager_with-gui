def add():
    from NewStar.Objects.User import User

    id = input('请输入id')
    id_name = input('请输入用户名')
    password = input('请输入密码')
    id_role = input('请输入学生角色')
    Class_id = input('请输入班级id')
    student_id = input('请输入学生id')
    user = User(id,id_name,password,id_role,Class_id,student_id)
    print(user)

