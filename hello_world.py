import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


# MyWidget继承自QWidget，最后show的是MyWidget对象
# 一个MyWidget对象含有一个QPushButton对象，就是一个按钮，要用clicked.connect()来设置按钮点击后调用的函数
# 一个MyWidget对象还有一个QLabel对象，这就只是一段话，也就是一个标签而已，需要setText来设置标签的内容
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        # 布局是先初始化一个QVBoxLayout对象然后再在这个对象上添加Widget
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":

    # 这个app有点像软件生命周期一样的概念
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
