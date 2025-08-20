FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY ./config ./config
COPY ./src ./src

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7777

ENV PYTHONUNBUFFERED=1
ENV APP_ENV=development
ENV PYTHONPATH=/app/src

WORKDIR /app/src
CMD ["python", "-m", "application.main"]
