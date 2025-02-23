FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/missing_number

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]