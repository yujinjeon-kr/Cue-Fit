import requests
import json

def generate_image_from_text(prompt):
    # OpenAI API 키 설정
    api_key = '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'  

    # 이미지 생성 요청 데이터
    data = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024",
        "model": "dall-e-3"
    }

    # OpenAI API 엔드포인트
    url = "https://api.openai.com/v1/images/generations"

    # 요청 헤더
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # API 요청 및 응답
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    # 생성된 이미지의 URL 추출
    image_url = response_json['data'][0]['url']

    # 이미지 저장
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open('generated_image.png', 'wb') as f:
            f.write(image_response.content)
        return 'generated_image.png'
    else:
        return 'Error: Image could not be retrieved.'
