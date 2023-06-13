from PySide6.QtWidgets import QApplication
from widget import Widget
import sys

app = QApplication(sys.argv)

window = Widget(app)
window.show()
window.resize(200,200)
app.exec()
