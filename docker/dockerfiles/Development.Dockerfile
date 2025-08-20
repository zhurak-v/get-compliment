FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

COPY ./config ./config
COPY ./src ./src

EXPOSE 7777

ENV PYTHONUNBUFFERED=1 \
    APP_ENV=development \
    PYTHONPATH=/app/src

WORKDIR /app/src
CMD ["python", "-m", "application.main"]