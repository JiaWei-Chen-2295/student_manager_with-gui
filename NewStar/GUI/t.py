import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, \
    QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QDialog, QDialogButtonBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette


class StudentSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("学生管理系统")
        self.setGeometry(100, 100, 800, 600)

        # 设置背景为淡黑色
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(30, 30, 30))
        self.setPalette(palette)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)

        # 左侧按钮栏
        left_layout = QVBoxLayout()
        self.buttons = ["查看", "添加", "修改", "删除"]
        for button_text in self.buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #3f3f3f;
                    color: white;
                    border-radius: 10px;
                    padding: 5px 10px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
            """)
            button.setFixedSize(100, 50)  # 缩小按钮并设置圆角
            left_layout.addWidget(button)
        layout.addLayout(left_layout)

        # 右侧展示区域
        right_layout = QVBoxLayout()

        # 下拉选择菜单
        self.select_menu = QComboBox()
        self.select_menu.addItem("选项一")
        self.select_menu.addItem("选项二")
        self.select_menu.currentIndexChanged.connect(self.show_table)
        right_layout.addWidget(self.select_menu)

        # 表格展示区
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)  # 示例列数
        self.table_widget.setHorizontalHeaderLabels(["姓名", "成绩"])
        right_layout.addWidget(self.table_widget)

        layout.addLayout(right_layout)

    def show_table(self, index):
        # 根据下拉菜单选项显示不同表格内容，这里仅为示例
        if index == 0:
            self.fill_table_with_data([{"name": "张三", "score": 90}, {"name": "李四", "score": 85}])
        elif index == 1:
            self.fill_table_with_data([{"subject": "数学", "grade": "A"}, {"subject": "英语", "grade": "B"}],
                                      headers=["科目", "等级"])

    def fill_table_with_data(self, data_list, headers=None):
        if headers:
            self.table_widget.setColumnCount(len(headers))
            self.table_widget.setHorizontalHeaderLabels(headers)
        self.table_widget.setRowCount(len(data_list))
        for row, data in enumerate(data_list):
            for col, key in enumerate(data.keys()):
                item = QTableWidgetItem(str(data[key]))
                self.table_widget.setItem(row, col, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentSystem()
    window.show()
    sys.exit(app.exec_())