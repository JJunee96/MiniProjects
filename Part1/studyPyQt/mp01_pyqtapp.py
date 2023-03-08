# PyQt 복습 - 직접 디자인 코딩 
import sys
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblMessage = QLabel('메세지: ', self)
        self.lblMessage.setGeometry(10, 5, 300, 50)

        btnOK = QPushButton('OK', self)
        btnOK.setGeometry(280, 250, 100, 40)
        # PyQt에서 이벤트를 시그널이라고 부름, 이벤트를 처리하는것을 슬롯이라 부름 
        btnOK.clicked.connect(self.btnOK_clicked) 

        self.setGeometry(300, 200, 400, 300)
        self.setWindowTitle('복습')
        self.show()

    def btnOK_clicked(self):
        self.lblMessage.clear()
        self.lblMessage.setText('메세지: OK!!')

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = qtApp()     # 지난번에는 MyApp
    sys.exit(app.exec_())