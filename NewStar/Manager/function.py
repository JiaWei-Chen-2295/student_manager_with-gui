from NewStar.Objects.User import User
def add():
    from NewStar.Objects.User import User
    id = input('请输入id')
    id_name = input('请输入用户名')
    password = input('请输入密码')
    id_role = input('请输入学生角色')
    Class_id = input('请输入班级id')
    student_id = input('请输入学生id')
    user = User(id_name,password,id_role,Class_id,student_id,id)
    print(user)
def view_all_information(user):
    if User.role == 'admin' or 'class_manager':
        print('学生姓名\t\t学生身份证号\t\t学生性别\t\t学生年龄\t\t学生学号\t\t学生班级\t\t学生专业')
        id_1 = User.user_id
        id_name_1 = User.username
        password_1 = User.password
        id_role_1 = User.role
        Class_id_1 = User.class_id
        student_id_1 = User.student_id
        information_1 = '%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t' % (id_1,id_name_1,password_1,id_role_1,
                                                                  Class_id_1,student_id_1)
        print(information_1)
def viewSelf_information(user_id):
    a = user_id
    if a.role == 'student':
        try:
            a.user_id == input('请输入您的id查看本人信息')
        except:
            print('该学生不存在')
        else:
            print('学生姓名\t\t学生身份证号\t\t学生性别\t\t学生年龄\t\t学生学号\t\t学生班级\t\t学生专业')
            id_name_1 = a.username
            password_1 = a.password
            id_role_1 = a.role
            Class_id_1 = a.class_id
            student_id_1 = a.student_id
            information_1 = '%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t' % (a, id_name_1, password_1, id_role_1,
                                                                      Class_id_1, student_id_1)
            print(information_1)
def update():
    if User.role == 'admin' or 'class_manager':
        pass



