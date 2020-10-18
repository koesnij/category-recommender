# fastText를 이용한 중고 판매 / 대여 게시글 카테고리 추천
Category Recommendation API with Flask & fastText

### /model-split.bin
fastText를 이용해 학습한 모델

### AWS에서 구동 중인 REST 서버
http://ec2-3-15-158-63.us-east-2.compute.amazonaws.com:5000

### 직접 서버 구동 방법
1. git clone
2. pip install -r requirements.txt
3. python server.py

### 사용 방법
Base URL : http://ec2-3-15-158-63.us-east-2.compute.amazonaws.com:5000

#### GET /recommender/<title>
  * Parameters
    * title (string) : 카테고리 예측을 할 게시물의 제목
  * Responses
    * { 'first': {'title': '카테고리 명', 'accuracy': '예상 확률'}, 'second': {'title': '카테고리 명', 'accuracy': '예상 확률'} }
    
    
##### 예시
- 요청 GET http://ec2-3-15-158-63.us-east-2.compute.amazonaws.com:5000/recommender/캠핑_용품_빌려드립니다
- 응답 {
  "second": {
    "title": "스포츠/레저",
    "accuracy": 0.9246283173561096
  },
  "first": {
    "title": "게임/취미",
    "accuracy": 0.03983434662222862
  }
}



