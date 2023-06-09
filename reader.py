import sys 
# intsall  pyusb package from pypi to read scanner  from the port and import it
import usb.core
import usb.util
from PySide6 import QtCore, QtWidgets


    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a text field and add it to the main window
        self.text_field = QtWidgets.QTextEdit(self)
        self.text_field.setGeometry(QtCore.QRect(100, 100, 200, 50))

        # Call the function that displays the name of the device connected to the USB port
        self.display_device_name()

    def display_device_name(self):
        # Find the device connected to the USB port
        dev = usb.core.find(idVendor=0x0c2e, idProduct=0x0989)
        if dev is None:
            raise ValueError('Device not found')
        else:
            print('Device found')
            print(dev)

        # Get the name of the device and display it in the text field
        device_name = usb.util.get_string(dev, dev.iProduct)
        self.text_field.setText(device_name)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
