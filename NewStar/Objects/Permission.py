from NewStar.Objects.User import User


class Role:
    def __init__(self,id,permission):
        self.id = id
        self.permission = permission
# class User:
#     def __init__(self,name,role,password):
#         self.name = name
#         self.role = role
#         self.password = []
#     def permission_distribution(self,permission):
#         return permission in self.role.permission

MANAGER_PERMISSION = ['add','view','update','delete']
INSTRUCTOR_PERMISSION = ['view','update']
STUDENT_PERMISSION = ['viewSelf','updateSelf']

user = User(1, 'jjk', 'vghvgh', 'admin', None, None)



# def main():
#     while True:
#         if manager_user.permission_distribution('add'):
#             add()
#         else:
#             print('您没有该权限')
#         if True:
#         view_information()
#         if manager_user.permission_distribution('update') or instructor_user.permission_distribution('update'):
#             update()
#         else:
#             print('您没有该权限')
#         if manager_user.permission_distribution('add'):
#             delete()
#         else:
#             print('您没有该权限')
# main()