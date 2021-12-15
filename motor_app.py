import sys
from PyQt5 import QtWidgets, QtGui
from motor import Ui_MainWindow
from PyQt5.QtSerialPort import QSerialPortInfo

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)                   # test.py altında ki setupUi() fonksiyon çalıştırılıyor ki altında ki elemanlar aktrılsın
                                                #self.ui ile test.py de ki elemanlar, metotlara ulaşılıyor.
        

        
        self.InitUi()
        self.serial_ports()
        self.ui.onoffButton.clicked.connect(self.on_off_button)      #topla butonu için
        self.ui.PWM_Slider.valueChanged.connect(self.slider_value_changed)

        self.ui.onoffButton.setCheckable(True)
        

    def InitUi(self):
        self.setWindowTitle("Motor App")
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.ui.onoffButton.setText('Pass')
        #self.ui.onoffButton.setStyleSheet('QPushButton {background-color: #18D80B}')
        self.ui.onoffButton.setStyleSheet("""
        QPushButton {background-color: #18D80B;} 
        QPushButton::checked{background-color: #FA1F1F;}
        """)

    def on_off_button(self):
        print("clicked")
        
       
        

    def slider_value_changed(self):
        slider_value = str(self.ui.PWM_Slider.value())
        self.ui.pwm_value.setText(slider_value)

    def serial_ports(self):
        """Serial port listeleme"""  
        serial_ports = QSerialPortInfo()
        for ports in serial_ports.availablePorts():
            self.ui.comboPORT.addItem(ports.portName())
        
        """Arduinoya data gönderme"""
        """Arduinoya"""

        




def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()
