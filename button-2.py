import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


# 这个例子包含Signals and Slots(信号与槽机制)
# 使用@Slot()表明这是一个槽函数
# @Slot() 服了，没使用这个居然也能照常运行
def say_hello():
    print("Button, clicked, hello!")


app = QApplication([])

# QPushButton里面的参数是按钮上会显示的文字
button = QPushButton("点我！")
button.clicked.connect(say_hello)
button.show()

app.exec()





