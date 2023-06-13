# from PySide6.QtCore import QSize
# from PySide6.QtGui import QAction,QIcon
# from PySide6.QtWidgets import QMainWindow,QToolBar,QPushButton,QStatusBar,QTextEdit
# #from PySide6 import QtWidgets

# class MainWindow(QMainWindow):
#     def __init__(self, app):
#         super().__init__()
#         self.app = app #declare an app member
#         self.setWindowTitle("Sycra QR Code Scanner") # window tittle 
#         self.resize(800, 600)
        

#         #menubar and menus
#         menu_bar = self.menuBar()
#         file_menu = menu_bar.addMenu("File")
#         quit_action = file_menu.addAction("Quit")
#         quit_action.triggered.connect(self.quit_app)

#         edit_menu = menu_bar.addMenu("Edit")
#         edit_menu.addAction("Copy")
#         edit_menu.addAction("Cut")
#         edit_menu.addAction("Paste")
#         edit_menu.addAction("Undo")
#         edit_menu.addAction("Redo")

#         # other menus 
#         menu_bar.addMenu("Window")
#         menu_bar.addMenu("Setting")
#         menu_bar.addMenu("Help")

#           #Working with toolbars
#         toolbar = QToolBar("My main toolbar")
#         toolbar.setIconSize(QSize(16, 16))
#         self.addToolBar(toolbar)

#         # Create a text editor widget and set it as the central widget of the window
#         self.text_editor = QTextEdit()
#         self.setCentralWidget(self.text_editor)
        

#         #Add the quit action to the toolbar
#         toolbar.addAction(quit_action)

#         action1 = QAction("Devices", self)
#         action1.setStatusTip("Status message for some action")
#         action1.triggered.connect(self.toolbar_button_click)
#         toolbar.addAction(action1)

#         action2 = QAction(QIcon("start.png"), "Some other action", self)
#         action2.setStatusTip("Status message for some other action")
#         action2.triggered.connect(self.toolbar_button_click)
#         #action2.setCheckable(True)
#         toolbar.addAction(action2)

#         toolbar.addSeparator()
#         toolbar.addWidget(QPushButton("Save"))

#         # Working with status bars
#         self.setStatusBar(QStatusBar(self))

#         button1 = QPushButton("BUTTON1")
#         button1.clicked.connect(self.button1_clicked)
#         self.setCentralWidget(button1)





#     def button1_clicked(self):
#         print("Clicked on the button")
#     def quit_app(self):
#         self.app.quit()    

#     def toolbar_button_click(self):
#         self.statusBar().showMessage("Message from my app",3000)    

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction,QIcon
from PySide6.QtWidgets import QMainWindow,QToolBar,QPushButton,QStatusBar,QTextEdit,QFileDialog

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Sycra QR Code Scanner") # window tittle 
        self.resize(800, 600)
        

        #menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # other menus 
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

          #Working with toolbars
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #Add the quit action to the toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Devices", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        #action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        
        # Create a save button and add it to the toolbar
        self.save_button = QPushButton("Save")
        toolbar.addWidget(self.save_button)

         # Connect the save button's clicked signal to a custom slot that saves the text to a file
        self.save_button.clicked.connect(self.save_text)

         # Working with status bars
        self.setStatusBar(QStatusBar(self))

         # Create a text editor widget and set it as the central widget of the window
         # This will add a textview in the middle of the mainwindow
        self.text_editor = QTextEdit()
        self.setCentralWidget(self.text_editor)

    def save_text(self):
         # Get the text from the text editor
         text = self.text_editor.toPlainText()

         # Open a file dialog to select a file name and location
         file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")

         # If a file name is selected, write the text to the file
         if file_name:
             with open(file_name, "w") as file:
                 file.write(text)

    def quit_app(self):
         self.app.quit()    

    def toolbar_button_click(self):
         self.statusBar().showMessage("Message from my app",3000)    
