import requests
import json

# 1단계에서 확인한 API 기본 정보
API_URL = "선택한 API의 엔드포인트 URL"
API_KEY = "발급받은 API 키"

# 예: MET API의 'flower' 검색과 유사한 요청
params = {
    "q": "검색어 또는 필요한 매개변수",
    "api_key": API_KEY
}

response = requests.get(API_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4)) # 데이터 구조 확인
else:
    print(f"Error: {response.status_code}")