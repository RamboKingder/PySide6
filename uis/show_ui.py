import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow

# 使用 pyside6-uic a.ui > b.py 可以将 QT Designer画出来的UI图转成python代码


# 自己画的MainWindow继承自QMainWindow类，且包含继承来的setupUi方法
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":

    # pyside6-uic untitled.ui>untitled.py

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

