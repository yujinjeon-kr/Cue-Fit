import pandas as pd
final_score_info = pd.read_excel('score_sheet.xlsx')

유형 = input("헬스 또는 PT를 입력하세요: ")

# 여기까지 services.html 활용 왜냐하면 여기서 헬스 또는 PT인지 입력을 받음

if 유형 == '헬스':
    # 헬스에 대한 정보 입력 받기
    회원권 = input("회원권을 입력하세요: ")
    가격 = input("가격을 입력하세요: ")
    주말여부 = input("주말 여부를 입력하세요 (Y/N): ")
    심야여부 = input("심야 여부를 입력하세요 (Y/N): ")
    data_PT = final_score_info[final_score_info['사업장 유형'] == "헬스"]
    
elif 유형 == 'PT':
    # PT에 대한 정보 입력 받기
    주말여부 = input("주말 여부를 입력하세요 (Y/N): ")
    심야여부 = input("심야 여부를 입력하세요 (Y/N): ")
    data_PT = final_score_info[final_score_info['사업장 유형'] == "PT"]


if 유형 == '헬스' :
  # 회원권에 따라 열 선택
  selected_price = data_PT[회원권]
  # 회원권 열의 값이 null인 행 제거
  data_PT = data_PT[data_PT[회원권].notna()]

  # 입력받은 가격보다 낮은 가격의 헬스장 필터링
  filtered_price = data_PT[(selected_price > 9800) & (selected_price < int(가격))]

  # 주말여부에 따라 필터링
  if 주말여부 == 'Y' :
      filtered_week = filtered_price[filtered_price['주말여부'] == 'Y']
        # 심야여부에 따라 필터링
      if 심야여부 == 'Y' :
        filtered_data = filtered_week[filtered_week['심야여부'] == 'Y']
      elif 심야여부 == 'N':
        filtered_data = filtered_week
  elif 주말여부 == 'N':
      filtered_week = filtered_price
      if 심야여부 == 'Y' :
        filtered_data = filtered_week[filtered_week['심야여부'] == 'Y']
      elif 심야여부 == 'N':
        filtered_data = filtered_week

elif 유형 =='PT' :
  # 주말여부에 따라 필터링
  if 주말여부 == 'Y' :
    filtered_week = data_PT[data_PT['주말여부'] == 'Y']
      # 심야여부에 따라 필터링
    if 심야여부 == 'Y' :
      filtered_data = filtered_week[filtered_week['심야여부'] == 'Y']
    elif 심야여부 == 'N':
      filtered_data = filtered_week
  elif 주말여부 == 'N' :
    filtered_week = data_PT
    if 심야여부 == 'Y' :
      filtered_data = filtered_week[filtered_week['심야여부'] == 'Y']
    elif 심야여부 == 'N':
      filtered_data = filtered_week

# 여기까지 services.html에 선택을 바탕으로 service2.html에서 선택을 해서 필터를 거침

우선순위 = input("선택한 카테고리를 입력하세요 (콤마로 구분): ").split(',')

선택카테고리 = filtered_data[['사업장명'] + 우선순위].sort_values(by=우선순위, ascending=False)

상위_30개 = 선택카테고리.sort_values(by=우선순위[0], ascending=False).head(30)

상위_10개 = 상위_30개.sort_values(by=우선순위[1],ascending=False).head(10)

상위_3개 = 상위_10개.sort_values(by=우선순위[2],ascending=False).head(3)


# 여기까지 service2.html을 선택을 바탕으로 service3.html에서 카테고리 선택을 받아서 그 이후에 recommend.html로 넘어감