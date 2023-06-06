FROM python:3.11.3-alpine3.18
ENV http_proxy http://proxy.esl.cisco.com
ENV https_proxy http://proxy.esl.cisco.com 
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apk add --no-cache ffmpeg
EXPOSE 800
ENTRYPOINT [ "./gunicorn.sh" ]
