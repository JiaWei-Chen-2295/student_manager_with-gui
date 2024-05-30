from NewStar.Dao.UserDao import UserDao
from NewStar.Objects.User import User
def add(user_name,password,id_role,Class_id,student_id):
    from NewStar.Objects.User import User
    user = User(user_name,password,id_role,Class_id,student_id)
    ud = UserDao()
    ud.insert(user)

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
    return all_user


def viewSelf_information(user_id):
    """
    先检测用户身份然后返回该用户信息
    Args:
        user_id: 传参获得用户查看id的信息

    Returns:指定id的全部信息

    """
    user_1 = []
    ud_1 = UserDao()
    user_list_1 = ud_1.selectById(user_id)
    try:
        c = {'id': user_list_1.user_id, 'id_name': user_list_1.username, 'id_role': user_list_1.role, 'Class_id': user_list_1.class_id,
             'student_id': user_list_1.student_id}
        user_1.append(c)
        return user_1
    except:
        return None

def update(user_id,user_name,password,id_role,Class_id,student_id,id):
    """

    Args:
        user_id: 传参获得要更新用户唯一标识
        user_name: 新用户姓名
        password: 新用户密码
        id_role: 新用户角色
        Class_id: 新用户班级id
        student_id:新用户学号
        id: 新唯一标识

    Returns:更新后的对象

    """
    ud_2 = UserDao()
    user_list_1 = ud_2.selectById(user_id)
    user_list_1.username = user_name
    user_list_1.password = password
    user_list_1.role = id_role
    user_list_1.class_id = Class_id
    user_list_1.student_id = student_id
    user_list_1.user_id = id
    user_list_1 = User(user_list_1.username, user_list_1.password, user_list_1.role, user_list_1.class_id, user_list_1.student_id, user_list_1.user_id)
    return user_list_1

def delete(user_id):
    """

    Args:
        user_id: 获得删除用户的唯一标识

    Returns:删除后的对象

    """
    ud_3 = UserDao()
    user_list_2 = ud_3.selectById(user_id)


    try:
        ud_3.drop(user_list_2)
    except:
        return -1





if __name__ == '__main__':
    a = delete(11)
