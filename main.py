import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QApp")
        button = QPushButton("Click me")

        self.setCentralWidget(button)


application = QApplication(sys.argv)

window = QMainWindow()
window.show()

application.exec()
