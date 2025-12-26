FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

# RUN apt update -y && apt install awscli -y
RUN pip install awscli

RUN apt-get update && pip install -r requirements.txt
CMD ["python3","app.py"]