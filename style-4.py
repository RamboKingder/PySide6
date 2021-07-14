import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel


if __name__ == "__main__":

    app = QApplication([])
    label = QLabel("This is a placeholder text")
    label.setAlignment(Qt.AlignCenter)

    # label.setText("what the fuck")

    label.resize(800, 500)

    # 可以使用类似CSS的QT样式表来定制我的Widget
    label.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;
    """)

    label.show()
    sys.exit(app.exec())

