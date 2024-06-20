리눅스 배포판에 맞는 도커 엔진 설치 - 배포판에 따라 패키지 관리자를 통해 설치
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/260a4c6d-19fb-49de-839a-3391585ad88a)
<br/>이미 있어서 인스톨도 패스!
<br/><br/> 
도커 다운되어 있는지 확인<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/0868cae0-40e2-4269-babb-bb06d00576f2)

잘 구현이 되는지 간단한 글자 구현부터 실행<br/>
index.html:
```<!DOCTYPE html>
<html>
<head>
  <title>Welcome to Docker Web Server</title>
</head>
<body>
  <h1>Hello from Docker!</h1>
  <p>This page is served by a Docker container.</p>
</body>
</html>
```
Dockerfile:
```# 베이스 이미지로 nginx를 사용합니다.
FROM nginx:latest

# 컨테이너 안의 /usr/share/nginx/html 디렉토리에 index.html 파일을 복사합니다.
COPY index.html /usr/share/nginx/html

# 포트 80을 외부에 노출합니다.
EXPOSE 80

# nginx 서버를 시작합니다.
CMD ["nginx", "-g", "daemon off;"]
```

도커 이미지 빌드<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/499d7d32-aece-428b-a25b-488806a93c7c)

도커 컨테이너 실행
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/f1626795-5227-4c8e-b3d2-1a08a9b31b36)

결과적으로 
![스크린샷 2024-06-19 110928](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/ee4a984c-db01-43df-8409-36cf128721e3)

잘배포되어 나옴
<br/><br/><br/>
이제 도커를 이용한 간단한 영화 추천 시스템 구현<br/>
<br/>프로젝트 구조 설정
```
movie-recommendation/
│
├── Dockerfile
├── requirements.txt
└── app.py
```
Dockerfile: 도커 이미지를 빌드하기 위한 설정 파일입니다.<br/>
requirements.txt: Python 패키지 의존성을 정의하는 파일입니다.<br/>
app.py: Flask 애플리케이션을 정의하는 Python 파일입니다.<br/>
<br/><br/>
여기서 다 작성하고 빌드후 실행(run)을 해보는데 컨테이너가 실행이 되지 않았다<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/12a9822b-731a-48c2-86bb-4e98cbed0bfd)
<br/>컨테이너 리스트를 보니 1코드로 실행되다 바로 종료되는 현상이었다<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/2bc27fb3-729d-4a00-acd0-80736a6f5129)
<br/> 바로 로그를 확인했고 Flask 애플리케이션 실행 중에 발생한 ImportError로, werkzeug 패키지에서 url_quote를 import할 수 없다는 오류였다 <br/>
해결책으로 패키지 업데이트를 시도했고<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/2351117e-1e47-4054-9291-683ea866debd)
<br/>경우에 따라 특정 버전의 Werkzeug가 필요할 수 있어 requirements.txt 파일에 Werkzeug의 특정 버전을 추가로 명시하였다<br/>
```
Flask==2.0.1
Werkzeug==2.0.1
```
<br/>그런 다음 Dockerfile에서 이 requirements.txt 파일을 사용하여 패키지를 설치<br/>
```
# 베이스 이미지로 Python 3.8을 사용합니다.
FROM python:3.8-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 필요한 패키지들을 설치합니다.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Flask 애플리케이션을 실행합니다.
CMD ["python", "app.py"]
```
<br/>혹시모를 이미지 빌드 중 캐시가 문제가 될 수 있어 캐시도 지웠다<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/34901e89-eee6-4f2b-99d4-c16d65af161d)
<br/> 그리고 다시 빌드와 컨테이너 실행 결과<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/c13302b8-70b7-4549-a8fe-72cb9a1a8c64)
<br/> 2라는 숫자가 떴고 그 의미는 애플리케이션 내에서 발생한 오류로 인해 컨테이너가 종료된 것이라 좀 더 명확한 로그 확인을 해봤다.<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/8c016012-8bd0-4ad0-8ede-ce9b3bd93b8e)
<br/>해당 오류는 Docker 컨테이너 안에서 실행하려는 app.py 파일을 찾지 못해서 발생한 것으로 수정을 하였다<br/>
Dockerfile:
```
# 베이스 이미지로 Python 3.8을 사용합니다.
FROM python:3.8-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리로 복사합니다.
COPY . .

# 필요한 패키지들을 설치합니다.
RUN pip install --no-cache-dir Flask

# Flask 애플리케이션을 실행합니다.
CMD ["python", "app.py"]
```
<br/>그리고 추천 페이지도 생성하고 메인과 연결하기 위해 추가 및 수정<br/>
app.py:<br/>
```
from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return '''
    <html>
    <head>
        <title>Movie Recommendation System</title>
    </head>
    <body>
        <h1>Welcome to Movie Recommendation System!</h1>
        <p>Click the button below to get a movie recommendation:</p>
        <form action="/recommend" method="get">
            <button type="submit">Get Recommendation</button>
        </form>
    </body>
    </html>
    '''

@app.route('/recommend')
def recommend_movie():
    movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump']
    recommended_movie = random.choice(movies)
    return jsonify({'movie': recommended_movie})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```
<br/> 마지막으로 기존 컨테이너 지우고 다시 빌드 및 컨테이너 실행<br/>
![image](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/5a707032-17b9-4ab9-8139-78073663a75c)<br/>
![시연 (2)](https://github.com/pladata-encore/DE30-4nd-5/assets/163955122/c5199591-2a38-4a94-8915-60d000c679e2)
<br/> 간단하지만 구현을 해냈다! 보면 버튼누를 때마다 다른 영화를 추천해준걸 볼 수 있다 이로써 도커에 대해 더 잘알게 된것같다.(복습개념)
