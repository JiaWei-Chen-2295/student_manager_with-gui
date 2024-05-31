"""
:description: 增删改查Major类
:author: Franklin
:version: 2.0
"""

from NewStar.Dao.MajorDao import MajorDao
from NewStar.Objects.Major import Major

def add(major_name):
    """

    Args:
        major_name: 专业传参

    Returns:返回新增专业类

    """
    major = Major(major_name)
    md = MajorDao()
    md.insert(major)
def view_all_major():
    """

    Returns:返回major类中所有对象

    """
    all_major = []
    md = MajorDao()
    major_list = md.selectAll()
    for i in major_list:
        a = {'id': i.major_id, 'major_name': i.major_name}
        all_major.append(a)
    return all_major

def viewSelf_major(major_id):
    """

    Args:
        major_id: 传参查询id

    Returns:返回指定id的major对象

    """
    major = []
    md = MajorDao()
    major_list = md.selectById(major_id)
    try:
        c = {'id': major_list.major_id, 'major_name':major_list.major_name}
        major.append(c)
        return major
    except:
        return None

def update(id,major_new_id,major_name):
    """

    Args:
        id: 更改对象id
        major_new_id: 对象新的id
        major_name: major类指定对象新的名字

    Returns:返回更新后的major类

    """
    md = MajorDao()
    try:
        major_list = md.selectById(id)
    except:
        return -1
    else:

        major_list.major_id = major_new_id
        major_list.major_name = major_name
        major_list = Major(major_list.major_id,major_list.major_name)
        md.update(major_list)

def delete(major_id):
    """

    Args:
        major_id: 指定删除对象id

    Returns:删除后的major类

    """
    md = MajorDao()
    major_list = md.selectById(major_id)
    try:
        md.drop(major_list)
    except:
        return -1

if __name__ == '__main__':
    a = update(3,3,'软件工程')

