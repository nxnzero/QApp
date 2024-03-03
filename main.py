import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

'''
QApplication - обработчик приложения
QWidget - базовый пустой виджет GUI
Widget - элемент для построения интерфейса(ов)
'''

application = QApplication(sys.argv) # sys.argv используется для аргументов ком строки

window = QWidget()
window.show() # Обязательный метод: по умолчанмю окно скрыто

# Start application
application.exec()
