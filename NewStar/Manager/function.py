from NewStar.Dao.UserDao import UserDao
from NewStar.Objects.User import User
def add(id,user_name,password,id_role,Class_id,student_id):
    from NewStar.Objects.User import User
    user = User(user_name,password,id_role,Class_id,student_id,id)
    return user
# TODO: 将对象属性返回字典
def view_all_information():
    """
    此函数首先检测用户身份
    若身份为管理员或辅导员
    允许查看所有学生信息

    Returns:返回以每个对象属性组成的字典为元素的列表
    """
    all_user = []
    ud = UserDao()
    user_list = ud.selectAll()
    for i in user_list:
        a = {'id': i.user_id, 'id_name':i.username, 'id_role':i.role, 'Class_id':i.class_id, 'student_id':i.student_id}
        all_user.append(a)
        if i.role == 'admin' or 'class_manager':
            return all_user
        else:
            return '您没有该权限'


def viewSelf_information(user_id):
    user_1 = []
    ud_1 = UserDao()
    user_list_1 = ud_1.selectById(user_id)
    if user_list_1.role == 'student':
        try:
            c = {'id': user_list_1.user_id, 'id_name': user_list_1.username, 'id_role': user_list_1.role, 'Class_id': user_list_1.class_id,
                 'student_id': user_list_1.student_id}
            user_1.append(c)
            return user_1
        except:
            return '该学生不存在'

def update(user_id,user_name,password,id_role,Class_id,student_id,id):
    ud_2 = UserDao()
    user_list_1 = ud_2.selectById(user_id)
    if user_list_1.role == 'admin' or 'class_manager':
        user_list_1.username = user_name
        user_list_1.password = password
        user_list_1.role = id_role
        user_list_1.class_id = Class_id
        user_list_1.student_id = student_id
        user_list_1.user_id = id
        user_list_1 = UserDao(user_name, password, id_role, Class_id, student_id, id)
    return user_list_1
def delete(user_id):
    ud_3 = UserDao()
    try:
        ud_3 = ud_3.drop(user_id)
        return ud_3
    except:
        return '该用户不存在'





