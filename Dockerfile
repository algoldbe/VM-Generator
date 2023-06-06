FROM python:3.11.3-alpine3.18
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apk add ffmpeg
EXPOSE 80
ENTRYPOINT [ "./gunicorn.sh" ]
