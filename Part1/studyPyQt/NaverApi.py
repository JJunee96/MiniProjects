# Naver Api 클래스 - Open Api : 인터넷을 통해 데이터를 전달 받음
from urllib.request import Request , urlopen
from urllib.parse import quote # 인코딩 기능과 동일한 함수(?)
import datetime   # 현재시간 사용을 위해서 
import json   # 결과는 json으로 리턴받을거임 (html형식(?))

class NaverApi:
    # 생성자 
    def __init__(self) -> None:
        print('Naver API 생성')

    # Naver API를 요청 함수 
    def get_request_url(self, url):
        req = Request(url)
        # Naver API 개인별 인증  (핵심 !!)
        req.add_header('X-Naver-Client-Id','tmPpeDTWaxllkvEikvr4')   # Naver(개발자) API 클라이언트 아이디
        req.add_header('X-Naver-Client-Secret','jtu3cKV1So')         # Naver(개발자) API 클라이언트 비밀번호

        try:
            res = urlopen(req)        # 요청 결과가 바로 돌아옴 
            if res.getcode() == 200:  # response OK
                print(f'[{datetime.datetime.now()}] NaverAPI 요청 성공')
                return res.read().decode('utf-8')
            else:
                print(f'[{datetime.datetime.now()}] NaverAPI 요청 실패')
                return None  # 실패 
        except Exception as e:
            print(f'[{datetime.datetime.now()}] 예외 발생 {e}')
            return None      # 실패 
    
    #  호출 함수 
    def get_naver_search(self, node, search, start, display):
        base_url = 'https://openapi.naver.com/v1/search'
        node_url = f'/{node}.json'
        params = f'?query={quote(search)}&start={start}&display={display}'

        url = base_url + node_url + params
        retData = self.get_request_url(url)

        if retData == None:
            return None
        else:
            return json.loads(retData)      # json으로 return. 

    # json으로 받은 데이터를 리스트로 변환 
    def get_post_data(self, post, outputs):
        title = post['title']
        description = post['description']
        originallink = post['originallink']
        link = post['link']

        # 문자열로 들어온걸 날짜 형식으로 변경(콘솔창에서 출력되는 맨 위의 날짜부분)
        pDate = datetime.datetime.strptime(post['pubDate'], '%a , %d %b %Y %H:%M:%S +0900')
        pubDate = pDate.strftime('%Y-%m-%d %H:%M:%S')    #2023-03-07 17:04:00 변경

        # outputs에 옮기기 - 내일 
