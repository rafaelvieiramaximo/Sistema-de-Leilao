FROM python:3.9-slim

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]