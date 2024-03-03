import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

application = QApplication(sys.argv) # sys.argv используется для аргументов ком строки

window = QWidget()
window.show() # Обязательный метод: по умолчанмю окно скрыто

# Start application
application.exec()
