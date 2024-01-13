import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re

# 1. 웹드라이버 접속
driver = webdriver.Chrome()

# 2. 데이터 불러오기
df = pd.read_excel('455_570.xlsx')

# 3. 정보 수집 준비
home_data = []  # 내용을 저장할 리스트

# 4. URL 접속 및 '더보기' 클릭
for url in df['Home URL']:
    try:
        # URL에 접속
        driver.get(url)
        time.sleep(5)  # 웹 페이지 로드를 위한 대기 시간

        # 5. 데이터 파싱
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # 데이터 가져오기
        reviews = []
        review_xpath_base = f'#app-root > div > div > div > div:nth-child(5) > div > div:nth-child(2)'
        #home_data.append(reviews)

        try:
            time.sleep(5)
            review = driver.find_element(By.CSS_SELECTOR, review_xpath_base).text
            time.sleep(2)

        except NoSuchElementException:
            review = "No review found"

        reviews.append(review)
        home_data.append(reviews)

    except Exception as e:
        print(f'Error while processing {url}: {e}')
        home_data.append([])


# 7. 데이터 저장
reviews_df = pd.DataFrame({
    'Home URL': df['Home URL'],
    'Info': home_data
})
reviews_df.to_excel('GYM_monday_info.xlsx', index=False)

# 웹드라이버 종료
driver.quit()