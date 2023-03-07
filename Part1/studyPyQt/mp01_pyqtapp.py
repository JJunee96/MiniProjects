# PyQt 복습
import sys
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblMessage = QLabel('메세지 : ', self)
        self.lblMessage.setGeometry(10, 10, 300, 50)

        btnOk = QPushButton('OK', self)
        btnOk.setGeometry(280, 250, 100, 40)
        # PyQt 이벤트(시그널) -> 이벤트핸들러(슬롯)
        btnOk.clicked.connect(self.btnOk_clicked)

        self.setGeometry(300, 200, 400, 300)
        self.setWindowTitle('복습PyQt')
        self.show()
    
    def btnOk_clicked(self):
        self.lblMessage.clear()
        self.lblMessage.setText('메세지 : OK!!!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    sys.exit(app.exec_())