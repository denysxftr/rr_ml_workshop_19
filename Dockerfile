FROM python:3.7.3

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

RUN pip install -e . && chmod +x ./production.sh

CMD ["./production.sh"]
