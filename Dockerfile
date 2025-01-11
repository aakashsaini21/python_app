FROM python:3.12.3
WORKDIR /app
COPY app.py .
CMD ["python3", "app.py"]