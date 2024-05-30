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
# def view_information():
#     print('-'*60)
#     print('学生姓名\t\t学生身份证号\t\t学生性别\t\t学生年龄\t\t学生学号\t\t学生班级\t\t学生专业')
#         id_1 = information['id']
#         idcard_1 = information['idcard']
#         gender_1 = information['gender']
#         age_1 = information['age']
#         id_study_1 = information['id_study']
#         Class_1 = information['Class']
#         profession_1 = information['profession']
#         information_1 = '%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t%s\t\t\t' % (id_1,idcard_1,gender_1,age_1,
#                                                                                                 id_study_1,Class_1,profession_1)
#         print(information_1)
#
if __name__ == '__main__':
    add()