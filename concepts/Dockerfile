FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY  jwt_authentication.py ./app/jwt_authentication.py


EXPOSE 8000

CMD ["uvicorn", "app.jwt_authentication:app", "--host", "0.0.0.0", "--port", "8000"]
