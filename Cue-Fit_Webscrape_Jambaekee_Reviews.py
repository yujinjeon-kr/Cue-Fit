import time

# selenium 3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

#selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
ENTER='/ue007'                                                                 

# DB 정보: MySQL
db = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='team2_final', charset='utf8mb4', use_unicode=True) # MySQL 연결
cont_explanation_len = 8191
cursor = db.cursor(pymysql.cursors.DictCursor)                              # Cursor Object 가져오기

# 로그인
driver.get('https://nid.naver.com/nidlogin.login')                          # 로그인 웹페이지 열기
my_id = 'jjunnew'                                                                  # 사용자 ID 입력
my_pw = 'nav0115ujin'                                                                  # 패스워드 입력
driver.execute_script("document.getElementsByName('id')[0].value = '" + my_id + "'")
time.sleep(0.5)                                                             # 에러시 부여할 딜레이 ([초])
driver.execute_script("document.getElementsByName('pw')[0].value = '" + my_pw + "'")
time.sleep(0.5)
button = driver.find_element(By.ID, "log.login")
button.click()
time.sleep(1)

# 카페 정보
url = 'https://cafe.naver.com/formsunmyeong'                                # 크롤링 할 카페 주소
club_id= 11100373                                                           # '잠백이' 카페 id
menu_id = 781                                                               # '서울' 게시판 id
qty = 1165                                                                  # 스크래핑할 게시물 수 (22년 1월 ~ 현재, 1165개 게시글) 

# 게시판 지정 및 클릭
driver.get(f'{url}?iframe_url=/ArticleList.nhn?search.clubid={club_id}%26search.menuid={menu_id}%26')
time.sleep(1)

driver.switch_to.frame("cafe_main")                                         # iframe으로 전환

# 카테고리 첫번째 글 클릭
driver.find_element(By.XPATH, '//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a[1]').click()
time.sleep(1)

# 크롤링 시작
for i in range (qty):
    print('[',i+1,'/',qty,']')                                               # 게시물 읽을 때마다 출력 [ 번호 / 1165 ]

    # 게시물 URL, ID, 작성일, 작성자 추출
    try:  
        cont_url = driver.find_element(By.XPATH, '//*[@id="spiButton"]').get_attribute('data-url')   # 게시물 URL      
        cont_id = cont_url.split('/')[-1]                                    # 게시물 ID
        cont_date = driver.find_element(By.CLASS_NAME, 'date').text          # 게시물 작성일
        print(cont_id,' ',cont_date)
        cont_author = driver.find_element(By.CLASS_NAME, 'nick_box').text    # 게시물 작성자
        
    except Exception as error:                                               # 로딩 실패시 재시도
        print(error)
        time.sleep(3)
        pass
    
    # 게시물 제목, 본문 추출
    if cont_id != None:
        cont_title = driver.find_element(By.CLASS_NAME, 'title_text').text   # 게시물 제목
        
        try:                                                                 # 게시물 본문  
            cont_explanation = driver.find_element(By.CLASS_NAME, 'se-main-container').text   # 본문이 se-main-container 타입인 경우
        except NoSuchElementException:                                       
            cont_explanation = driver.find_element(By.CLASS_NAME, 'ContentRenderer').text     # 본문이 ContentRenderer 타입인 경우
        except Exception as error:                                           # 로딩 실패시 재시도
            print(error)
            pass
        cont_explanation = cont_explanation[0:8191]                          # 본문이 긴 경우 잘라넣기
        cont_explanation_encoded = cont_explanation.encode('utf-8', 'ignore')# DB 입력 전 인코딩하기

        # MySQL에 연동
        sql_insert = (f'INSERT INTO cafe_jambaekee (cont_id, cont_title, cont_url, cont_author, cont_date, cont_explanation) VALUES (%s, %s, %s, %s, %s, %s)')
        val = (cont_id, cont_title, cont_url, cont_author, cont_date, cont_explanation)
        cursor.execute(sql_insert,val)                                       # MySQL 실행
        db.commit()                                                          # MySQL 서버에 확정 반영하기 db.commit()

    try:
        # 다음 페이지 이동
        driver.find_element(By.LINK_TEXT, '다음글').click()
        time.sleep(3)
    except Exception as error:                                               # 로딩 실패시 재시도
        print(error)
        pass

db.close()
