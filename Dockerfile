FROM mcr.microsoft.com/playwright/python:v1.38.0

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN playwright install --with-deps

ENTRYPOINT ["pytest"]
