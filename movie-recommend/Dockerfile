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
