import LedFiles
import sys
from Led import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
from pyftdi.gpio import GpioAsyncController,GpioMpsseController,GpioMpsseController
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
#from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QVBoxLayout

class Led(QMainWindow):
    def __init__(self):
        super(Led, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.gpio_in, self.gpio_out = GpioMpsseController(), GpioMpsseController()
        self.gpio_in.configure('ftdi:///1', direction=0x0000, frequency=10e6)
        self.gpio_out.configure('ftdi:///1', direction=0xFFFF, frequency=10e6)

        self.D00PushButton = self.ui.D00PushButton
        self.D01PushButton = self.ui.D01PushButton
        self.D02PushButton = self.ui.D02PushButton
        self.D03PushButton = self.ui.D03PushButton
        self.D04PushButton = self.ui.D04PushButton
        self.D05PushButton = self.ui.D05PushButton
        self.D06PushButton = self.ui.D06PushButton
        self.D07PushButton = self.ui.D07PushButton
        self.D08PushButton = self.ui.D08PushButton
        self.D09PushButton = self.ui.D09PushButton
        self.D10PushButton = self.ui.D10PushButton
        self.D11PushButton = self.ui.D11PushButton
        self.D12PushButton = self.ui.D12PushButton
        self.D13PushButton = self.ui.D13PushButton
        self.D14PushButton = self.ui.D14PushButton
        self.D15PushButton = self.ui.D15PushButton

        self.out = 0 

        self.D00PushButton.clicked.connect(self.D00PushButtonState)
        self.D01PushButton.clicked.connect(self.D01PushButtonState)
        self.D02PushButton.clicked.connect(self.D02PushButtonState)
        self.D03PushButton.clicked.connect(self.D03PushButtonState)


    def D00PushButtonState(self):
        if(self.D00PushButton.isChecked()):
            self.gpio_out.write(self.out + 1)
            self.out = self.out + 1
        else:
            self.gpio_out.write(self.out - 1)
            self.out = self.out - 1

    def D01PushButtonState(self):
        if(self.D01PushButton.isChecked()):
            self.gpio_out.write(self.out + 2)
            self.out = self.out + 2
        else:
            self.gpio_out.write(self.out - 2)
            self.out = self.out + 2

    def D02PushButtonState(self):
        if(self.D02PushButton.isChecked()):
            self.gpio_out.write(self.out + 3)
        else:
            self.gpio_out.write(self.out - 3)

    def D03PushButtonState(self):
        if(self.D03PushButton.isChecked()):
            self.gpio_out.write(self.out + 4)
        else:
            self.gpio_out.write(self.out - 4)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Led()
    window.show()

    sys.exit(app.exec())