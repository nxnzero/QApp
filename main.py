import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QApp")

        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked on me")
        self.button.setEnabled(False)

        self.setWindowTitle("HeyQA")


application = QApplication(sys.argv)

window = MainWindow()
window.show()

application.exec()
