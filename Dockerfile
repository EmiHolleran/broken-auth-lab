FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install flask flask-limiter
CMD ["python", "app.py"]
