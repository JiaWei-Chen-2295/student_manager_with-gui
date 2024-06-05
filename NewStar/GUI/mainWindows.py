import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, \
    QTableWidgetItem, QFormLayout, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

from NewStar.Manager.StudentManager import add, update, delete


class StudentManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('学生管理系统')
        self.setGeometry(100, 100, 800, 600)

        # 设置窗口背景颜色为淡黑色，适当透明
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30, 200))  # 200为透明度
        self.setPalette(palette)

        self.initUI()

    def initUI(self):
        # 创建中央Widget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # 左侧按钮区域
        leftLayout = QVBoxLayout()
        self.viewButton1 = self.createButton('查看用户', self.showTable1)
        self.viewButton2 = self.createButton('查看学生', self.showTable2)
        self.viewButton3 = self.createButton('查看班级', self.showTable3)
        self.viewButton4 = self.createButton('查看专业', self.showTable4)
        # self.modifyButton1 = self.createButton('修改/添加用户', lambda: self.showForm('用户'))
        self.modifyButton2 = self.createButton('修改/添加学生', lambda: self.showForm('学生'))
        # self.insertButton1 = self.createButton('修改/添加班级', lambda: self.showForm('班级'))
        # self.insertButton2 = self.createButton('修改/添加专业', lambda: self.showForm('专业'))
        self.deleteButton = self.createButton('删除', lambda: self.deleteRecord())
        leftLayout.addWidget(self.viewButton1)
        leftLayout.addWidget(self.viewButton2)
        leftLayout.addWidget(self.viewButton3)
        leftLayout.addWidget(self.viewButton4)
        # leftLayout.addWidget(self.modifyButton1)
        leftLayout.addWidget(self.modifyButton2)
        # leftLayout.addWidget(self.insertButton1)
        # leftLayout.addWidget(self.insertButton2)
        leftLayout.addWidget(self.deleteButton)
        leftLayout.addStretch()  # 占据剩余空间

        # 创建一个容器Widget并设置布局
        buttonContainer = QWidget()
        buttonContainer.setLayout(leftLayout)
        buttonContainer.setFixedWidth(150)
        buttonContainer.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.3);  # 设置半透明背景
                border-radius: 15px;
            }
        """)

        # 右侧展示区域
        rightLayout = QVBoxLayout()

        # 文字标签
        self.formLabel = QLabel()
        self.formLabel.setStyleSheet("color: white; font-size: 16px; padding: 10px;")
        rightLayout.addWidget(self.formLabel)
        self.formLabel.hide()  # 初始隐藏标签

        # 表格展示
        self.tableWidget = QTableWidget()
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #333;
                color: white;
                border-radius: 10px;
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #555;
                color: white;
                padding: 5px;
            }
        """)
        rightLayout.addWidget(self.tableWidget)

        # 表单展示
        input_style = "background-color: #333; color: white; border-radius: 5px; padding: 5px;"
        # form_fields_lists = [
        #     ['id', '姓名', '密码', '角色', 'class_id', 'student_id'],
        #     ['id', '姓名', '一卡通', 'class_id'],
        #     ['id', '班级名', '专业id'],
        #     ['id', '专业名']
        # ]
        self.formLayout = QFormLayout()
        self.noInput = QLineEdit()
        self.idInput = QLineEdit()
        self.nameInput = QLineEdit()
        self.passwordInput = QLineEdit()
        self.classIdInput = QLineEdit()
        self.cardInput = QLineEdit()
        self.classIdInput = QLineEdit()
        self.noInput.setStyleSheet(input_style)
        self.idInput.setStyleSheet(input_style)
        self.nameInput.setStyleSheet(input_style)
        self.passwordInput.setStyleSheet(input_style)
        self.cardInput.setStyleSheet(input_style)
        self.classIdInput.setStyleSheet(input_style)
        self.formLayout.addRow('序号:', self.idInput)
        self.formLayout.addRow('姓名:', self.nameInput)
        self.formLayout.addRow('一卡通:', self.cardInput)
        self.formLayout.addRow('class_id:', self.classIdInput)

        self.formWidget = QWidget()
        self.formWidget.setLayout(self.formLayout)
        rightLayout.addWidget(self.formWidget)
        self.formWidget.hide()  # 初始隐藏表单

        # 标签展示，用于不同选项显示不同内容
        self.label = QLabel()
        self.label.setStyleSheet("color: white;")
        rightLayout.addWidget(self.label)

        # 提交按钮
        self.submitButton = QPushButton('提交')
        self.submitButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                border-radius: 20px; 
                color: white;
                font-size: 16px;
                margin: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.submitButton.clicked.connect(self.submitForm)
        rightLayout.addWidget(self.submitButton)
        self.submitButton.hide()  # 初始隐藏提交按钮

        # 提交按钮2
        self.submitButton2 = QPushButton('提交')
        self.submitButton2.setStyleSheet("""
                   QPushButton {
                       background-color: #4CAF50; 
                       border-radius: 15px; 
                       color: white;
                       font-size: 16px;
                       margin: 5px;
                   }
                   QPushButton:hover {
                       background-color: #45a049;
                   }
               """)
        self.submitButton2.clicked.connect(self.submitForm2)
        rightLayout.addWidget(self.submitButton2)
        self.submitButton2.hide()  # 初始隐藏提交按钮

        # 总体布局
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(buttonContainer)
        mainLayout.addLayout(rightLayout)

        centralWidget.setLayout(mainLayout)

    def createButton(self, text, callback):
        button = QPushButton(text)
        button.setFixedSize(130, 40)  # 设置按钮大小以适应左边栏宽度
        button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                border-radius: 15px; 
                color: white;
                font-size: 16px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        button.clicked.connect(callback)
        return button

    def showTable1(self):
        from NewStar.Manager import Usermanager
        headers = ['id', '姓名', '密码', '角色', 'class_id', 'student_id']
        data = Usermanager.view_all_information()
        self.showTable(headers, data)

    def showTable2(self):
        from NewStar.Manager import StudentManager
        headers = ['id', '姓名', '一卡通', 'class_id']
        data = StudentManager.view_all_student()
        self.showTable(headers, data)

    def showTable3(self):
        from NewStar.Manager import SchoolClassManager
        headers = ['id', '班级名', '专业id']
        data = SchoolClassManager.view_all_information()
        self.showTable(headers, data)

    def showTable4(self):
        from NewStar.Manager import MajorManager
        headers = ['id', '专业名']
        data = MajorManager.view_all_major()
        self.showTable(headers, data)

    def deleteRecord(self):
        self.formWidget.hide()
        self.label.hide()
        self.formWidget.show()
        self.idInput.show()
        self.submitButton.hide()
        self.submitButton2.show()
        self.nameInput.hide()
        self.cardInput.hide()
        self.classIdInput.hide()
        self.idInput.setPlaceholderText("请输入序号,目前仅支持删除学生")

    def showTable(self, headers, data):
        self.formWidget.hide()
        self.label.hide()
        self.submitButton.hide()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(data):
            for col, key in enumerate(item):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item[key])))
        self.tableWidget.show()

    def submitForm(self):
        id_value = self.idInput.text()
        name_value = self.nameInput.text()
        card_value = self.cardInput.text()
        class_id_value = self.classIdInput.text()

        # 将输入的值保存到数据库或打印到控制台
        if id_value == "":
            try:
                add(name_value, card_value, class_id_value)
                QMessageBox.information(self, "Info", "添加成功")
            except Exception:
                QMessageBox.information(self, "Warning", "添加错误。请检查你的输入")

        else:
            try:
                id_value = int(id_value)
                update(id_value, name_value, card_value, class_id_value)
                QMessageBox.information(self, "Info", "修改成功")
            except Exception:
                QMessageBox.information(self, "Warning", "修改错误。请检查你的输入")

        # 根据表单类型，执行相应的逻辑
    def submitForm2(self):
        id_value = self.idInput.text()
        if id_value == '':
            QMessageBox.information(self, "Info", "id不可为空")
        else:
            id_value = int(id_value)
            try:
                delete(id_value)
                QMessageBox.information(self, "Info", "删除成功")
            except:
                QMessageBox.information(self, "警告", "删除失败")

    def showForm(self, formType):
        QMessageBox.information(self, "Info", "如果输入序号即为修改，不输入序号即为添加")
        self.formWidget.show()
        self.tableWidget.hide()
        self.label.hide()

        self.idInput.show()
        self.formLayout.labelForField(self.idInput).show()
        self.submitButton.show()  # 显示提交按钮
        # # 显示提示文字
        # self.idInput.clear()
        # self.nameInput.clear()
        # self.ageInput.clear()
        # self.formWidget.show()
        # self.tableWidget.hide()

        # self.showInfoBox("如果输入序号即为修改，不输入序号即为添加")
        self.idInput.setVisible(True)
        self.formLayout.labelForField(self.idInput).setVisible(True)
        self.noInput.setPlaceholderText("如果输入序号即为修改，不输入序号即为添加")
        self.idInput.setPlaceholderText("请输入序号")
        self.nameInput.setPlaceholderText("请输入姓名")
        self.cardInput.setPlaceholderText("请输入一卡通卡号")
        self.classIdInput.setPlaceholderText("请输入 Class_id ,点击查看班级以对应id数字")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentManagementSystem()
    window.show()
    sys.exit(app.exec_())