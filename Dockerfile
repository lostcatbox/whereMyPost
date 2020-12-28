FROM python:3.7.6

COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 7979
CMD ["python","manage.py","runserver","0.0.0.0:7979"]
