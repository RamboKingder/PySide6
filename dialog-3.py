import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import Slot


# QDialog就是弹出的对话框，可以连接一些QPushButton之类的，也可以在对话框中定义更复杂的东西
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        # 再添加一个QLineEdit对象和一个QPushButton对象
        self.edit = QLineEdit("Write your name here")
        self.button = QPushButton("Show Greetings")

        # 使用QVBoxLayout来垂直布局我的widgets
        layout = QVBoxLayout()  # 第一次知道在类内可以定义非self.的东西
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)  # setLayout()方法继承自父类QDialog

        self.button.clicked.connect(self.greetings)

    @Slot()  # 虽然不写槽装饰器好像也行，但是为了规范还是写上
    def greetings(self):
        # 类内函数可以访问self的东西，QLineEdit对象的text()方法会返回输入的内容
        print(f"Hello, {self.edit.text()}")


# 这里还是加上这一句把，万一我要用别的地方引入这里定义的Form类呢
if __name__ == "__main__":

    app = QApplication([])
    form = Form()
    form.show()
    app.exec()
