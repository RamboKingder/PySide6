import sys
from PySide6.QtWidgets import QApplication, QLabel

# 其实这句可有可无，因为我肯定不会在外部import label-0
# if __name__ == "__main__":

app = QApplication([])

# QLabel也属于一种Widget
label = QLabel("Hello world! I'm happy to learn PySide6.")
# label.resize(800, 500)

label.show()

app.exec()  # 进入QT主循环并执行QT代码，事实上只有运行到这一行label才会显示出来

# sys.exit(app.exec()) # 跟直接app.exec()效果是一样的


