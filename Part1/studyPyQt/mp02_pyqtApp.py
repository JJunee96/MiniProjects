# QtDesigner 디자인 사용 
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    count = 0 # 클릭 횟수 카운트 변수

    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/mainApp.ui', self)

        # QtDesigner 에서 구성한 위젯 시그널 만듬
        self.btnOK.clicked.connect(self.btnOKClicked)
        self.btnPOP.clicked.connect(self.btnPOPClicked)

    def btnOKClicked(self):   # 슬롯 함수 
        self.count += 1
        self.lblMessage.clear()
        self.lblMessage.setText(f'메세지: OK!!+{self.count}')
    
    def btnPOPClicked(self):
        QMessageBox.about(self, 'popup', '까꿍!')

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = qtApp()     
    ex.show()
    sys.exit(app.exec_())