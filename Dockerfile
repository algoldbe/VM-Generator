FROM python:3-alpine3.15
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "./gunicorn.sh" ]
