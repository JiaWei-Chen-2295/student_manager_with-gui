from nicegui import ui

# 定义自定义CSS样式
custom_css = """
body {
    background-image: url('https://img2.imgtp.com/2024/05/30/bGec7gRG.png'); /* Replace URL with your image */
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    font-family: Arial, sans-serif;
}

.login-container {
    max-width: 400px;
    margin: auto;
    padding: 40px;
    background-color: rgba(255, 255, 255, 0.9); /* Add transparency for better visibility */
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-align: center;
}

.login-logo img {
    max-width: 500px;
    margin-bottom: 300px;
}

.login-container img {
    max-width: 100px;
    margin-bottom: 20px;
}

.login-container h1 {
    text-align: center;
    font-size: 40px; /* 放大字体 */
    color: #333333;
    margin-bottom: 30px;
}

.login-container .input-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login-container {
    width: 500px; /* Adjust the width */
    height: 400px; /* Adjust the height */
    margin: auto;
    padding: 40px;
    background: rgba(255, 255, 255, 0.3); /* Adjust the opacity to control frosted effect */
    backdrop-filter: blur(10px); /* Adjust the blur radius for frosted effect */
    border-radius: 20px; /* Increase the border-radius for rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-align: center;
}

.login-container .login-input {
    width: calc(100% - 20px);
    padding: 15px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
    box-sizing: border-box;
}

.login-container .login-button {
    width: 100%;
    padding: 15px;
    background-color: #007bff;
    border: none;
    border-radius: 5px;
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.login-logo img {
    max-width: 80%;
    margin-bottom: 30px;
}

.login-container {
    background-color: #218838; /* Change hover background color */
}

.login-container .login-button:hover {
    background-color: #0056b3;
}

.signup-button {
    background-color: #28a745;
}

.login-container .agreement {
    margin-top: 20px;
    font-size: 12px;
    color: #666666;
}
/* Adjusting text color to white */
.login-container * {
    color: white;
}

/* Centering input fields */
.login-input {
    margin: 0 auto;
}

/* Styling the registration link */
.signup-link {
    color: #28a745; /* Green color */
    text-decoration: underline;
    cursor: pointer;
    transition: color 0.3s;
}
"""

# 注入自定义CSS
ui.add_head_html(f'<style>{custom_css}</style>')

# 创建登录界面
def signup():
    ui.notify("即将跳转注册", color='positive')


with ui.card().classes('login-container'):
    # ui.image('https://img2.imgtp.com/2024/05/30/b0titUDy.png').classes('login-logo')  # 添加Logo
    # ui.image('https://img2.imgtp.com/2024/05/30/cqyLvvDd.png').classes('login-logo')  # 添加Logo
    # ui.image('https://img2.imgtp.com/2024/05/30/bGec7gRG.png').classes('login-logo')  # 添加Logo
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