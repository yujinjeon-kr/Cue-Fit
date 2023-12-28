# NLP 기반 허위 리뷰 페널티 정책을 통한 헬스장 추천 서비스 '큐피트(Cue-Fit)'


## 프로젝트 소개
서울시 강남구 헬스장의 실제 고객 리뷰를 자연어처리로 분석하여, 이용자 맞춤 헬스장을 추천하는 추천 서비스입니다. 


## 개발 기간
 - 2023.11.1 ~ 2023.12.20


### 멤버 구성
 - 조하연(PL/TA): 모델링, 알고리즘 구현
 - 박서우(AA): 서비스 기획, 마케팅 기획, PPT 제작 및 발표
 - 전유진(DA): 데이터 수집 및 전처리, 데이터 시각화, 알고리즘 설계 및 구현
 - 최지연(DA): 데이터 수집, 데이터 시각화, 알고리즘 설계 및 구현
 - 황승현(TA): 모델링, 웹사이트 개발


### 개발 환경
 - 운영 체제: Windows 10
 - 데이터베이스: MySQL
 - 개발 언어: Python 3.8, SQL
 - 개발 도구: VS Code, Google Colab, django, Chat GPT-3, Excel, UiPath
 - 분석 및 시각화: Power BI, matplotlib, Seaborn


## 파일 안내
### 1. 웹스크레핑 소스코드
  - Cue-Fit_Webscape_Naver_GeneralInfo.ipynb
  - Cue-Fit_Webscape_Naver_Reviews.ipynb
  - Cue-Fit_Webscape_Naver_urls.ipynb
  - Cue-Fit_Webscape_Kakao_Reviews.ipynb
  - Cue-Fit_Webscape_Kakao_urls.ipynb
  - Cue-Fit_Jambaekee_Reviews.py
    
### 2. 탐색적 데이터 분석 및 시각화
  - Cue-Fit_Gyms_EDA.ipynb
    
### 3. 자연어처리 소스코드
  - Cue-Fit_LDA_TopicModeling.ipynb
  - Cue-Fit_Vader_Sentiment_Analysis.ipynb
  - Cue-Fit_Find_FalseReview.ipynb
  - Cue-Fit_Extract_Equipments.ipynb
  - 
### 4. 추천 알고리즘 소스코드
  - Cue-Fit_Recommendation.ipynb
  - 
### 5. UI/웹사이트 구현 소스코드 및 데모
  - Cue-Fit_UI.ipynb
  - Cue-Fit Service_FrondEnd 폴더
  - Cue-Fit Service_demo.mp4

### 엑셀 데이터 파일
  - category.xlsx
  - modify.xlsx
  - oneword.xlsx
  - stopwords.xlsx
  - word_list.xlsx
  - Machine_Substitution.xlsx
  - Score_Rate_Table.xlsx
