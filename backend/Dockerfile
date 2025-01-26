FROM python:3.11-slim

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN apt-get update && apt-get install -y locales \
    && locale-gen pl_PL.UTF-8 \
    && dpkg-reconfigure locales
    
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
