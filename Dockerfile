FROM python:3.9.1-alpine

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY wsgi.py wsgi.py
COPY blog ./blog

RUN flask init-db
RUN flask create-users
RUN flask create-articles

EXPOSE 5000

CMD ["python", "wsgi.py"]