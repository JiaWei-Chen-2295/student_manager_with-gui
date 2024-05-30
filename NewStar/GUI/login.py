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
    width: 500px; /* Adjust the width */
    height: 400px; /* Adjust the height */
    margin: auto;
    padding: 40px;
    background: rgba(255, 255, 255, 0.3); /* Adjust the opacity to control frosted effect */
    backdrop-filter: blur(10px); /* Add frosted glass effect */
    border-radius: 20px; /* Increase the border-radius for rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-align: center;
}

.login-container .input-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login-container .login-input {
    width: 100%; /* Change the width to 100% */
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
    text-align: center; /* Center align button text */
}

.login-button {
    text-align: center;
}

.login-container .login-button:hover {
    background-color: #0056b3;
}

.signup-button {
    background-color: #28a745;
}

.login-container {
    margin-top: 20px;
    font-size: 12px;
    color: #666666;
}

.agreement {

    margin-top: 20px;
    font-size: 12px;
    color: #666666;
    text-align: center;

}

/* Adjusting text color to white */
.login-container * {
    color: white;
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