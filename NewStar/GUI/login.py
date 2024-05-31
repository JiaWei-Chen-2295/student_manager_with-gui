from nicegui import ui

def get_css():
    with open('login_css', 'r') as file:
        custom_css = file.read()
        return custom_css
# 定义自定义CSS样式
custom_css = get_css()

# 注入自定义CSS
ui.add_head_html(f'<style>{custom_css}</style>')

# 创建登录界面
def signup():
    ui.notify("即将跳转注册", color='positive')


with ui.card().classes('login-container'):
    ui.label('登录').classes('h1')
    with ui.column().classes('input-container'):
        username = ui.input(label='用户名').props('dense clearable').classes('login-input')
        password = ui.input(label='密码', password=True).props('dense clearable').classes('login-input')
    ui.button('登录', on_click=lambda: login(username.value, password.value)).classes('login-button')
    ui.label('登录即表示您同意我们的服务条款和隐私政策').classes('agreement')
    ui.label('没有账号？').classes('agreement')
    ui.button('注册', on_click=signup).classes('signup-link')

def login(username, password):
    # 在这里处理登录逻辑
    if username == 'admin' and password == 'admin':
        ui.notify('登录成功', color='positive')
    else:
        ui.notify('用户名或密码错误', color='negative')



# 启动NiceGUI应用
ui.run(port=8080)