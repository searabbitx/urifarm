FROM python:3.10-alpine
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
CMD ["python", "-u",  "app.py"]
