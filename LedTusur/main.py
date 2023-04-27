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

        self.EnterLabel  = self.ui.EnterLabel
        self.lineEdit = self.ui.lineEdit
        self.OkPushButton = self.ui.OkPushButton
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
        self.D04PushButton.clicked.connect(self.D04PushButtonState)
        self.D05PushButton.clicked.connect(self.D05PushButtonState)
        self.D06PushButton.clicked.connect(self.D06PushButtonState)
        self.D07PushButton.clicked.connect(self.D07PushButtonState)
        self.D08PushButton.clicked.connect(self.D08PushButtonState)
        self.D09PushButton.clicked.connect(self.D09PushButtonState)
        self.D10PushButton.clicked.connect(self.D10PushButtonState)
        self.D11PushButton.clicked.connect(self.D11PushButtonState)
        self.D12PushButton.clicked.connect(self.D12PushButtonState)
        self.D13PushButton.clicked.connect(self.D13PushButtonState)
        self.D14PushButton.clicked.connect(self.D14PushButtonState)
        #self.D15PushButton.clicked.connect(self.D15PushButtonState)
        self.OkPushButton.clicked.connect(self.push_OkPushButton)


    def D00PushButtonState(self):
        if(self.D00PushButton.isChecked()):
            self.out = self.out + 128
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 128
            self.gpio_out.write(self.out)

    def D01PushButtonState(self):
        if(self.D01PushButton.isChecked()):
            self.out = self.out + 256
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 256
            self.gpio_out.write(self.out)

    def D02PushButtonState(self):
        if(self.D02PushButton.isChecked()):
            self.out = self.out + 512
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 512
            self.gpio_out.write(self.out)

    def D03PushButtonState(self):
        if(self.D03PushButton.isChecked()):
            self.out = self.out + 1024
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 1024
            self.gpio_out.write(self.out)

    def D04PushButtonState(self):
        if(self.D04PushButton.isChecked()):
            self.out = self.out + 2048
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 2048
            self.gpio_out.write(self.out)

    def D05PushButtonState(self):
        if(self.D05PushButton.isChecked()):
            self.out = self.out + 4096
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 4096
            self.gpio_out.write(self.out)

    def D06PushButtonState(self):
        if(self.D06PushButton.isChecked()):
            self.out = self.out + 8192
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 8192
            self.gpio_out.write(self.out)

    def D07PushButtonState(self):
        if(self.D07PushButton.isChecked()):
            self.out = self.out + 16384
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 16384
            self.gpio_out.write(self.out)

    def D08PushButtonState(self):
        if(self.D08PushButton.isChecked()):
            self.out = self.out + 1
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 1
            self.gpio_out.write(self.out)

    def D09PushButtonState(self):
        if(self.D09PushButton.isChecked()):
            self.out = self.out + 2
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 2
            self.gpio_out.write(self.out)

    def D10PushButtonState(self):
        if(self.D10PushButton.isChecked()):
            self.out = self.out + 4
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 4
            self.gpio_out.write(self.out)

    def D11PushButtonState(self):
        if(self.D11PushButton.isChecked()):
            self.out = self.out + 8
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 8
            self.gpio_out.write(self.out)

    def D12PushButtonState(self):
        if(self.D12PushButton.isChecked()):
            self.out = self.out + 16
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 16
            self.gpio_out.write(self.out)

    def D13PushButtonState(self):
        if(self.D13PushButton.isChecked()):
            self.out = self.out + 32
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 32
            self.gpio_out.write(self.out)

    def D14PushButtonState(self):
        if(self.D14PushButton.isChecked()):
            self.out = self.out + 64
            self.gpio_out.write(self.out)
        else:
            self.out = self.out - 64
            self.gpio_out.write(self.out)

    #def D15PushButtonState(self):
    #    if(self.D15PushButton.isChecked()):
    #        self.gpio_out.write(self.out + 128)
    #        self.out = self.out + 128
    #    else:
    #        self.gpio_out.write(self.out - 128)
    #        self.out = self.out - 128


    def control_type_lineEdit(self, lineEdit):
        data = lineEdit.text()
        if not data.isdigit() and data != '':
            self.lineEdit.setStyleSheet("background-color: red")

        if (int(data) > 32767) or (int(data) < 0):
            self.lineEdit.setStyleSheet("background-color: red")
            end
        else:
            self.lineEdit.setStyleSheet("background-color: white")
        return data


    def push_OkPushButton(self):
        self.out = 0
        data = self.control_type_lineEdit(self.lineEdit)
        data = int(data)
        self.gpio_out.write(self.out)
        self.D00PushButton.setChecked(False)
        self.D01PushButton.setChecked(False)
        self.D02PushButton.setChecked(False)
        self.D03PushButton.setChecked(False)
        self.D04PushButton.setChecked(False)
        self.D05PushButton.setChecked(False)
        self.D06PushButton.setChecked(False)
        self.D07PushButton.setChecked(False)
        self.D08PushButton.setChecked(False)
        self.D09PushButton.setChecked(False)
        self.D10PushButton.setChecked(False)
        self.D11PushButton.setChecked(False)
        self.D12PushButton.setChecked(False)
        self.D13PushButton.setChecked(False)
        self.D14PushButton.setChecked(False)

        if data == 0:
            self.out = 0
            self.gpio_out.write(self.out)
            self.D00PushButton.setChecked(False)
            self.D01PushButton.setChecked(False)
            self.D02PushButton.setChecked(False)
            self.D03PushButton.setChecked(False)
            self.D04PushButton.setChecked(False)
            self.D05PushButton.setChecked(False)
            self.D06PushButton.setChecked(False)
            self.D07PushButton.setChecked(False)
            self.D08PushButton.setChecked(False)
            self.D09PushButton.setChecked(False)
            self.D10PushButton.setChecked(False)
            self.D11PushButton.setChecked(False)
            self.D12PushButton.setChecked(False)
            self.D13PushButton.setChecked(False)
            self.D14PushButton.setChecked(False)
        if data % 2 != 0:
            self.out = self.out + 128
            self.gpio_out.write(self.out)
            self.D00PushButton.setChecked(True)
            data = data - 1
            self.testNaStepen(data)
        else:
            self.testNaStepen(data)
                    

    def testNaStepen(self, data):
        if data >= pow(2, 14):
            self.out = self.out + 64
            self.gpio_out.write(self.out)
            self.D14PushButton.setChecked(True)
            data = data - 16384
        if data >= pow(2, 13):
            self.out = self.out + 32
            self.gpio_out.write(self.out)
            self.D13PushButton.setChecked(True)
            data = data - 8192
        if data >= pow(2, 12):
            self.out = self.out + 16
            self.gpio_out.write(self.out)
            self.D12PushButton.setChecked(True)
            data = data - 4096
        if data >= pow(2, 11):
            self.out = self.out + 8
            self.gpio_out.write(self.out)
            self.D11PushButton.setChecked(True)
            data = data - 2048
        if data >= pow(2, 10):
            self.out = self.out + 4
            self.gpio_out.write(self.out)
            self.D10PushButton.setChecked(True)
            data = data - 1024
        if data >= pow(2, 9):
            self.out = self.out + 2
            self.gpio_out.write(self.out)
            self.D09PushButton.setChecked(True)
            data = data - 512
        if data >= pow(2, 8):
            self.out = self.out + 1
            self.gpio_out.write(self.out)
            self.D08PushButton.setChecked(True)
            data = data - 256
        if data >= pow(2, 7):
            self.out = self.out + 16384
            self.gpio_out.write(self.out)
            self.D07PushButton.setChecked(True)
            data = data - 128
        if data >= pow(2, 6):
            self.out = self.out + 8192
            self.gpio_out.write(self.out)
            self.D06PushButton.setChecked(True)
            data = data - 64
        if data >= pow(2, 5):
            self.out = self.out + 4096
            self.gpio_out.write(self.out)
            self.D05PushButton.setChecked(True)
            data = data - 32
        if data >= pow(2, 4):
            self.out = self.out + 2048
            self.gpio_out.write(self.out)
            self.D04PushButton.setChecked(True)
            data = data - 16
        if data >= pow(2, 3):
            self.out = self.out + 1024
            self.gpio_out.write(self.out)
            self.D03PushButton.setChecked(True)
            data = data - 8
        if data >= pow(2, 2):
            self.out = self.out + 512
            self.gpio_out.write(self.out)
            self.D02PushButton.setChecked(True)
            data = data - 4
        if data >= pow(2, 1):
            self.out = self.out + 256
            self.gpio_out.write(self.out)
            self.D01PushButton.setChecked(True)
            data = data - 2



     

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Led()
    window.show()

    sys.exit(app.exec())