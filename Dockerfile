FROM python:3.10

RUN apt-get update && \
apt-get install -y sqlite3

COPY requirements.txt /tmp/requirements.txt
COPY notes /notes

WORKDIR /notes

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

CMD ["sh", "-c", "sleep 10 && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]








