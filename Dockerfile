FROM ubuntu
ENV http_proxy http://proxy.esl.cisco.com
ENV https_proxy http://proxy.esl.cisco.com
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && apt-get install -y ffmpeg && apt-get install -y python3 && apt-get install -y python3-pip 
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 800
ENTRYPOINT [ "./gunicorn.sh" ]
