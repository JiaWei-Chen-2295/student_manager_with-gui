"""
:description: 增删改查user类
:author: Franklin
:version: 2.0
"""
from NewStar.Dao.SchoolClassDao import SchoolClassDao
from NewStar.Objects.SchoolClass import SchoolClass


def add(class_name,major_id):
    sc = SchoolClass(class_name,major_id)
    sd = SchoolClassDao()
    sd.insert(sc)

# TODO: 将schoolclass对象属性返回字典

def view_all_information():
    """
    若身份为管理员
    允许查看所有学生信息

    Returns:返回以每个对象属性组成的字典为元素的列表
    """
    all_sc = []
    sd = SchoolClassDao()
    sc_list = sd.selectAll()
    for i in sc_list:
        a = {'class_name': i.class_name, 'class_id':i.class_id, 'major_id':i.major_id}
        all_sc.append(a)
    return all_sc


def viewSelf_class_information(class_id):
    """
    先检测用户身份然后返回该用户信息
    Args:
        class_id: 传参获得班级类查看id的信息

    Returns:指定id的全部信息

    """
    sc_1 = []
    sd_1 = SchoolClassDao()
    sc_list = sd_1.selectById(class_id)
    try:
        c = {'class_name': sc_list.class_name, 'class_id': sc_list.class_id,  'major_id': sc_list.major_id}

        sc_1.append(c)
        return sc_1
    except:
        return None


def update(class_id,class_new_id,class_name,major_id):
    """

    Args:
        class_id: 更改对象id
        class_new_id: 对象新的id
        major_id: major类指定对象新的名字

    Returns:返回更新后的class类

    """
    sd = SchoolClassDao()
    try:
        sc_list = sd.selectById(class_id)
    except:
        return -1
    else:

        sc_list.class_id = class_new_id
        sc_list.class_name = class_name
        sc_list.major_id = major_id
        sc_list = SchoolClass(class_new_id,class_name,major_id)
        sd.update(sc_list)

def delete(class_id):
    """

    Args:
        class_id: 指定删除对象id

    Returns:删除后的class类

    """
    sd = SchoolClassDao()
    sc_list = sd.selectById(class_id)
    try:
        sd.drop(sc_list)
    except:
        return -1

if __name__ == '__main__':
    update(7,8,'rty',3)