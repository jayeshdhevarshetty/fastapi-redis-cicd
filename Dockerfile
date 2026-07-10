FROM python:3.12

WORKDIR /app

COPY requirnment.txt .

RUN pip install -r requirnment.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]