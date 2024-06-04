# 页面 启动！！！
from nicegui import ui

from NewStar.GUI.login import login_page

login_page()
ui.run(port=8080)