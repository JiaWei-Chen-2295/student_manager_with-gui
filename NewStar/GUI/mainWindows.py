import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, QFormLayout, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

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
        self.modifyButton = self.createButton('修改', self.showForm)
        self.deleteButton = self.createButton('删除', self.deleteRecord)
        self.moreButton = self.createButton('更多', self.showMore)
        leftLayout.addWidget(self.viewButton1)
        leftLayout.addWidget(self.viewButton2)
        leftLayout.addWidget(self.viewButton3)
        leftLayout.addWidget(self.viewButton4)
        leftLayout.addWidget(self.modifyButton)
        leftLayout.addWidget(self.deleteButton)
        leftLayout.addWidget(self.moreButton)
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
        self.formLayout = QFormLayout()
        self.nameInput = QLineEdit()
        self.ageInput = QLineEdit()
        self.nameInput.setStyleSheet("background-color: #333; color: white; border-radius: 5px; padding: 5px;")
        self.ageInput.setStyleSheet("background-color: #333; color: white; border-radius: 5px; padding: 5px;")
        self.formLayout.addRow('姓名:', self.nameInput)
        self.formLayout.addRow('年龄:', self.ageInput)
        self.formWidget = QWidget()
        self.formWidget.setLayout(self.formLayout)
        rightLayout.addWidget(self.formWidget)

        self.formWidget.hide()  # 初始隐藏表单

        # 标签展示，用于不同选项显示不同内容
        self.label = QLabel()
        self.label.setStyleSheet("color: white;")
        rightLayout.addWidget(self.label)

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
        headers = ['id', '专业']
        data = MajorManager.view_all_major()
        self.showTable(headers, data)

    def showTable(self, headers, data):
        self.formWidget.hide()
        self.label.hide()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        for row, item in enumerate(data):
            for col, key in enumerate(item):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item[key])))
        self.tableWidget.show()

    def showForm(self):
        self.tableWidget.hide()
        self.label.hide()
        self.formWidget.show()

    def deleteRecord(self):
        # 删除记录逻辑
        pass

    def showMore(self):
        # 更多功能逻辑
        pass

    def onComboBoxChange(self, index):
        if index == 0:
            self.showOption1()
        elif index == 1:
            self.showOption2()
        elif index == 2:
            self.showOption3()

    def showOption1(self):
        self.formWidget.hide()
        self.tableWidget.hide()
        self.label.setText("这是选项1的内容")
        self.label.show()

    def showOption2(self):
        self.formWidget.hide()
        self.tableWidget.hide()
        self.label.setText("这是选项2的内容")
        self.label.show()

    def showOption3(self):
        self.formWidget.hide()
        self.tableWidget.hide()
        self.label.setText("这是选项3的内容")
        self.label.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentManagementSystem()
    window.show()
    sys.exit(app.exec_())