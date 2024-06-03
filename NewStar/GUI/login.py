from nicegui import ui

from NewStar.Manager.loginUserManager import loginCheck
from NewStar.Manager.Usermanager import add


def login_page():
    # Define custom CSS style
    custom_css = get_css()

    # Inject custom CSS
    ui.add_head_html(f'<style>{custom_css}</style>')

    # Create login form
    login_container = ui.card().classes('login-container')
    with login_container:
        ui.label('登录').classes('h1')
        with ui.column().classes('input-container'):
            username = ui.input(label='用户名').props('dense clearable').classes('login-input')
            password = ui.input(label='密码', password=True).props('dense clearable').classes('login-input')
        ui.button('登录', on_click=lambda: login(username.value, password.value)).classes('login-button')
        ui.label('登录即表示您同意我们的服务条款和隐私政策').classes('agreement')
        ui.label('没有账号？').classes('agreement')
        ui.button('注册', on_click=lambda: register(login_container)).classes('signup-link')


def get_css():
    with open('new_login_css.txt', 'r', encoding='utf-8') as file:
        custom_css = file.read()
        return custom_css



# Create registration form
def register_user(username, p1, p2):
    if username != None or p1 != p2:
        ui.notify("注册失败")
        return
    else:
        try:
            add(username, p1, 'student', None, None)
            ui.notify("注册成功")
            login_page()
        except:
            ui.notify("注册失败")
            return

def register(login_container):
    login_container.clear()  # Clear the login form
    ui.notify("即将跳转注册", color='positive')
    ui.label('注册').classes('h1')
    with ui.column().classes('input-container'):
        username = ui.input(label='用户名').props('dense clearable').classes('login-input')
        password = ui.input(label='密码', password=True).props('dense clearable').classes('login-input')
        confirm_password = ui.input(label='确认密码', password=True).props('dense clearable').classes('login-input')
        ui.button('注册',on_click=lambda: register_user(username.value, password.value, confirm_password.value)).classes(
            'login-button')


# 定义创建新页面的函数
def create_new_page():
    page = ui.page(path='/new_page')  # 指定新页面的路径
    grid = ui.grid()
    with grid.column():
        with ui.sidebar(width='20%'):
            ui.button('查询所有')
            ui.button('新增')
            ui.button('账号绑定')
    with grid.column():
        ui.label('这是新页面')
    page.add(grid)  # 将网格添加到页面中

def login(username, password):
    # Handle login logic here
    if loginCheck(username, password):
        ui.notify('登录成功', color='positive')
        # create_new_page()  # Call function to create and display new page
    else:
        ui.notify('用户名或密码错误', color='negative')

# Run the NiceGUI application
login_page()
ui.run(port=8080)