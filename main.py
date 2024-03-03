import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

application = QApplication(sys.argv)

window = QWidget()
window.show()

application.exec()
