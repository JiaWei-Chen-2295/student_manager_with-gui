"""
:description: 增删改查Student类
:author: Franklin
:version: 2.0
"""

from NewStar.Dao.StudentDao import StudentDao
from NewStar.Objects.Student import Student

def add(student_name,student_card_num,student_class_id):
    """

    Args:
        student_name: 传参学生名字
        student_card_num:传参学生学生证号
        student_class_id: 传参学生班级号

    Returns:增加后的student对象

    """
    student = Student(student_name,student_card_num,student_class_id)
    sd = StudentDao()
    sd.insert(student)

def view_all_student():
    """

    Returns:返回student类中所有对象

    """
    all_student = []
    sd = StudentDao()
    student_list = sd.selectAll()
    for i in student_list:
        a = {'student_id':i.id,'student_name': i.name, 'student_card_num': i.card_num,'student_class_id':i.class_id}
        all_student.append(a)
    return all_student

def viewSelf_student(student_id):
    """

    Args:
        student_id: 查看学生学号

    Returns:该id所有信息

    """
    student = []
    sd = StudentDao()
    student_list = sd.selectById(student_id)
    try:
        c = {'student_id':student_list.id,'student_name': student_list.name, 'student_card_num':student_list.card_num,'student_class_id':student_list.class_id}
        student.append(c)
        return student
    except:
        return None

def update(student_id,student_name,student_card_num,student_class_id):
    """

        Args:
            id: 更改对象id
            major_name: major类指定对象新的名字

        Returns:返回更新后的major类

        """
    sd = StudentDao()
    try:
        student_list = sd.selectById(student_id)
    except:
        return -1
    else:

        student_list.name = student_name
        student_list.card_num = student_card_num
        student_list.class_id = student_class_id
        sd.update(student_list)

def delete(id):
    """

    Args:
        major_id: 指定删除对象id

    Returns:删除后的major类

    """
    sd = StudentDao()
    student_list = sd.selectById(id)
    try:
        sd.drop(student_list)
    except:
        return -1

if __name__ == '__main__':
    delete(8)
    print(view_all_student())