# QtDesigner 디자인 사용 
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverApi import *
from urllib.request import urlopen
import webbrowser   # 웹브라우저 모듈

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/NaverAPIMovie.ui', self)
        self.setWindowIcon(QIcon('./studyPyQt/movie.png'))

        # 검색 버튼 클릭시그널 / 슬롯함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        # 검색어 입력 후 엔터를 치면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    def tblResultDoubleClicked(self):
        # row = self.tblResult.currentIndex().row()
        # column = self.tblResult.currentIndex().column()
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text()   # url 링크컬럼 변경
        webbrowser.open(url)    # 네이버 영화 웹 사이트 오픈

    def txtSearchReturned(self):
        self.btnSearchClicked()

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.warning(self ,'경고', '영화명를 입력하세요.')
            return
        else:
            api = NaverApi()    # NavereApi 클래스 객체 생성
            node ='movie'        # movie로 변경하면 영화검색 
            display = 100

            result= api.get_naver_search(node, search, 1, display)
            print(result) #-- 출력값이 많으면 불편 // 개발할때 확인용으로 사용
            # 테이블위젯에 출력 기능
            items = result['items'] # json결과 중 itmes 아래 배열만 추출
            self.makeTable(items)

    # 테이블 위젯에 데이터 표시 -- 네이버 영화 결과 변경
    def makeTable(self, items) -> None: 
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)  # 단일선택
        self.tblResult.setColumnCount(7)    # 컬럼갯수 변경
        self.tblResult.setRowCount(len(items))  # 현재100개 행 생성
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '개봉년도', '감독', '배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 70)    # 개봉년도
        self.tblResult.setColumnWidth(4, 50)    # 평점
        # 컬럼 데이터를 수정금지
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)    # 컬럼수정 금지

        for i, post in enumerate(items):    # 0, 영화
            title = self.replaceHtmlTag(post['title']) # HTML 특수문자 변환 / 영어제목 가져오기 추가
            subtitle = post['subtitle']
            title = f'{title}({subtitle})'
            pubDate = post['pubDate']
            director = post['director'].replace('|', ',')[:-1]
            actor = post['actor'].replace('|', ',')[:-1]    # [:-1] 파이썬에서만 가능!!

            userRating = post['userRating']
            link = post['link']
            img_url = post['image']
            # 포스터 이미지 추가
            if img_url != '': # 빈값이면 포스터가 없음
                data = urlopen(img_url).read()  # 2진데이터 - 네이버영화에 있는 이미지 다운, 텍스트 형태 데이터
                image = QImage()    # 이미지 객체
                image.loadFromData(data)
                # QTableWidget 이미지를 그냥 넣을 수 없음. QLabel() 집어넣은뒤 QLabel -> QTableWidget
                imglabel = QLabel()
                imglabel.setPixmap(QPixmap(image))

                # data를 이미지로 저장가능!
                # f = open(f'./studyPyQt/temp/image_{i+1}.png', mode ='wb') # 파일쓰기
                # f.write(data)
                # f.close()


            # imageUrl = urlopen(post['image']).read()
            # image = QPixmap()
            # image.loadFromData(imageUrl)
            # imgLabel = QLabel()
            # imgLabel.setPixmap(image)
            # imgLabel.setGeometry(0, 0, 60, 100)
            # imgLabel.resize(60, 100)

            # setItem(행, 열, 넣을데이터)
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))
            self.tblResult.setItem(i, 6, QTableWidgetItem(img_url))
            if img_url != '':
                self.tblResult.setCellWidget(i, 6, imglabel)
                self.tblResult.setRowHeight(i, 110) # 포스터가 있으면 쉘 높이를 늘림
            else:
                self.tblResult.setItem(i, 6, QTableWidgetItem('No Poster!'))

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<').replace('&gt;', '>').replace('<b>', '').replace('</b>', '').replace('&apos;', "'").replace('&quot;', '"')  # quotation mark 쌍따옴표
        # 변환 안된 특수문자가 나타나면 여기 추가

        return result



if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = qtApp()     
    ex.show()
    sys.exit(app.exec_())