import sys

from PyQt5.QtWidgets import QApplication
from nicegui import ui

from NewStar.GUI.mainWindows import StudentManagementSystem
from NewStar.Manager.loginUserManager import loginCheck
from NewStar.Manager.Usermanager import add

css = """
/* 设置背景图片铺满页面 */
body {
    background-image: url('https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1msKXW.img');
    background-size: cover;
    background-position: center;
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white; /* 设置全局字体颜色为白色 */
}

/* 毛玻璃效果卡片 */
.login-container {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 10px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    padding: 40px; /* 增大内边距 */
    width: 100%;
    max-width: 600px; /* 调整最大宽度 */
    box-sizing: border-box;
}

/* 调整标签的样式 */
.h1 {
    font-size: 2.5em; /* 增大字体 */
    margin-bottom: 30px;
    text-align: center;
    color: white;
}

.input-container {
    display: flex;
    flex-direction: column;
    gap: 20px; /* 增大输入框之间的间距 */
}

.login-input {
    width: 100%;
    padding: 15px; /* 增大输入框内边距 */
    font-size: 1.2em; /* 增大字体 */
    color: white;
    border: 1px solid #ddd;
    box-sizing: border-box;
}

.login-button {
    width: 100%;
    padding: 15px; /* 增大按钮内边距 */
    font-size: 1.2em; /* 增大字体 */
    cursor: pointer;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    text-align: center;
    margin-top: 20px;
}

.login-button:hover {
    background-color: #0056b3;
}

.login-input::placeholder {

	color: rgba(255, 255, 255, 0.7);

}

.agreement {
    margin-top: 20px; /* 增大上外边距 */
    text-align: center;
    font-size: 1em; /* 增大字体 */
    color: white;
}

.signup-link {
    background-color: #28a745;
    font-size: 1em; /* 缩小字体 */
    padding: 10px; /* 缩小内边距 */
    width: auto; /* 宽度自适应内容 */
    margin: 10px auto 0; /* 居中 */
    cursor: pointer;
    color: white;
    border: none;
    border-radius: 5px;
}

.signup-link:hover {
    background-color: #218838;
}
"""

def login_page():
    # 获取 CSS 样式
    # custom_css = get_css()
    # 注入 CSS
    ui.add_head_html(f'<style>{css}</style>')
    # 登录表单
    login_container = ui.card().classes('login-container')
    with login_container:
        ui.label('登录').classes('h1')
        with ui.column().classes('input-container'):
            username = ui.input(label='用户名').props('dense clearable').classes('login-input')
            password = ui.input(label='密码', password=True).props('dense clearable').classes('login-input')
        ui.button('登录', on_click=lambda: login(username.value, password.value, login_container)).classes('login-button')
        ui.label('登录即表示您同意我们的服务条款和隐私政策').classes('agreement')
        ui.label('没有账号？').classes('agreement')
        ui.button('注册', on_click=lambda: register(login_container)).classes('signup-link')

def get_css():
    with open('new_login_css.txt', 'r', encoding='utf-8') as file:
        custom_css = file.read()
        return custom_css

# 注册按钮逻辑
def register_user(username, p1, p2, register_container):
    if username == None or p1 != p2:
        ui.notify("注册失败")
        return
    else:
        try:
            add(username, p1, 'student', None, None)
            ui.notify("注册成功")
            register_container.clear()
            login_page()
            ui.run(port=8080)
        except:
            ui.notify("注册失败", color='negative')
            return

# 注册表单
def register(login_container):
    login_container.clear()  # Clear the login form
    register_container = ui.column().classes('input-container')
    ui.notify("即将跳转注册", color='positive')
    with register_container:
        ui.label('注册').classes('h1')
        with ui.column().classes('input-container'):
            username = ui.input(label='用户名').props('dense clearable').classes('login-input')
            password = ui.input(label='密码', password=True).props('dense clearable').classes('login-input')
            confirm_password = ui.input(label='确认密码', password=True).props('dense clearable').classes('login-input')
            ui.button('注册',on_click=lambda: register_user(username.value, password.value, confirm_password.value, register_container)).classes(
                'login-button')

# 登录按钮逻辑
def login(username, password, login_container):
    if loginCheck(username, password):
        ui.notify('登录成功', color='positive')
        login_container.clear()
        ui.label('现在请关闭浏览器').classes('h1')
        app = QApplication(sys.argv)
        window = StudentManagementSystem()
        window.show()
        sys.exit(app.exec_())
    else:
        ui.notify('用户名或密码错误', color='negative')

if __name__ == '__main__':
    login_page()
    ui.run(port=8080)
