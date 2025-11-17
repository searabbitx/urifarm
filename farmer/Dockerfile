FROM python:3.10-alpine
COPY . /opt/app
WORKDIR /opt/app
RUN apk add moreutils
RUN pip install -r requirements.txt
RUN chmod 755 ./merge.sh
RUN mkdir out
RUN mkfifo stash.txt
RUN touch out/paths.txt
CMD ["python", "-u", "app.py"]
