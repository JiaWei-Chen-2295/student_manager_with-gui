class Role:
    def __init__(self,name,permission):
        self.name = name
        self.permission = permission
class User:
    def __init__(self,name,role,password):
        self.name = name
        self.role = role
        self.password = []
    def permission_distribution(self,permission):
        return permission in self.role.permission

manager_permission = ['add','view','update','delete']
instructor_permission = ['view','update']
student_permission = ['viewSelf','updateSelf']

manager_role = Role('manager',manager_permission)
instructor_role = Role('instructor',instructor_permission)
student_role = Role('student',student_permission)

manager_user = User('2022',manager_role,123)
instructor_user = User('2023',instructor_role,456)
student_user = User('2024',student_role,789)



try:
    print(manager_user.permission_distribution('add'))
    print(instructor_user.permission_distribution('add'))
except:
    print('False')

database = []

def menu():
    print('-'*60)
    print('学生管理系统1.0')
    print('1.添加学生信息')
    print('2.查询学生信息')
    print('3.更新学生信息')
    print('4.删除学生信息')
    print('5.退出系统')
    cmd = input('请输入您的选择')
    print('-'*60)
    return cmd

def add():
    id = input('请输入学生姓名')
    idcard = input('请输入学生身份证号')
    gender = input('请输入学生性别')
    age = input('请输入学生年龄')
    id_study = input('请输入学生学号')
    Class = input('请输入学生班级')
    profession = input('请输入学生专业')
    new_student = {'id': id,'idcard' : idcard, 'gender': gender, 'age':age,'id_study' : id_study,'Class' : Class,'profession' : profession}
    database.append(new_student)
    print('添加成功')
    print('-'*60)

def view_information():
    print('-'*60)
    print('学生姓名\t\t学生身份证号\t\t学生性别\t\t学生年龄\t\t学生学号\t\t学生班级\t\t学生专业')
    for information in database:
        id_1 = information['id']
        idcard_1 = information['idcard']
        gender_1 = information['gender']
        age_1 = information['age']
        id_study_1 = information['id_study']
        Class_1 = information['Class']
        profession_1 = information['profession']
        information_1 = '%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t%s\t\t\t' % (id_1,idcard_1,gender_1,age_1,
                                                                                                id_study_1,Class_1,profession_1)
        print(information_1)
def update():
    print('-'*60)
    for new_information in database:
        new_information['id'] = input('请输入学生姓名')
        new_information['idcard'] = input('请输入学生身份证号')
        new_information['gender'] = input('请输入学生性别')
        new_information['age'] = input('请输入学生年龄')
        new_information['id_study'] = input('请输入学生学号')
        new_information['Class'] = input('请输入学生班级')
        new_information['profession'] = input('请输入学生专业')
        print(database)
def delete():
    try:
        a = input('请输入删除学生id_study')
        b = database.index(a)
        index_information = database[b]
        database.remove(index_information)
    except:
        print('此学生不存在')
    finally:
        print('操作完成')


def main():
    while True:
        cmd = menu()
        if cmd == '1':

            if manager_user.name == 'zhang' and manager_user.password == 123:
                if manager_user.permission_distribution('add'):
                    add()
            else:
                print('您没有该权限')
        elif cmd == '2':
            view_information()
        elif cmd == '3':
            if manager_user.permission_distribution('update') or instructor_user.permission_distribution('update'):
                update()
            else:
                print('您没有该权限')
        elif cmd == '4':
            if manager_user.permission_distribution('add'):
                delete()
            else:
                print('您没有该权限')
        elif cmd == '5':
            break
main()





