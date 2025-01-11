FROM python:3.12.3
WORKDIR /app
COPY app1.py .
CMD ["python3", "app1.py"]
