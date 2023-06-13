from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore, QtWidgets

class Widget(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app 
        self.text_field = QtWidgets.QTextEdit(self)
        self.text_field.setGeometry(QtCore.QRect(100, 100, 400, 400))
        self.setWindowTitle("Barcodescanner")