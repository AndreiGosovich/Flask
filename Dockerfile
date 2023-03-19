FROM python:3.9.1-alpine

WORKDIR /app

RUN pip install --upgrade pip

RUN apk add --no-cache bash

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x wait-for-postgres.sh

EXPOSE 5000

CMD ["python", "wsgi.py"]