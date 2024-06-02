from nicegui import ui

def get_css():
    with open('new_login_css.txt', 'r', encoding='utf-8') as file:
        custom_css = file.read()
        return custom_css

# Define custom CSS style
custom_css = get_css()

# Inject custom CSS
ui.add_head_html(f'<style>{custom_css}</style>')

# Create registration form
def register_user(value, value1, value2):
    pass


def register():
    login_container.clear()  # Clear the login form
    ui.notify("即将跳转注册", color='positive')
    ui.label('注册').classes('h1')
    with ui.column().classes('input-container'):
        username = ui.input(label='用户名').props('dense clearable').classes('login-input')
        password = ui.input(label='密码', password=True).props('dense clearable').classes('login-input')
        confirm_password = ui.input(label='确认密码', password=True).props('dense clearable').classes('login-input')
        ui.button('注册',on_click=lambda: register_user(username.value, password.value, confirm_password.value)).classes(
            'login-button')


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
    ui.button('注册', on_click=register).classes('signup-link')

def login(username, password):
    # Handle login logic here
    if username == 'admin' and password == 'admin':
        ui.notify('登录成功', color='positive')
    else:
        ui.notify('用户名或密码错误', color='negative')

# Run the NiceGUI application
ui.run(port=8080)