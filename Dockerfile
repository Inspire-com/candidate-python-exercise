FROM alpine:latest
RUN apk add --no-cache python3 py-pip vim

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python3 -m pip install -r requirements.txt

CMD python3 -m pytest && python3 app.py 0.0.0.0
