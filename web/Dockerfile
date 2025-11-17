FROM python:3.10-alpine
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
CMD ["python", "-m", "gunicorn", "app:app", "-b", "0.0.0.0:3000", "--workers", "10"]
