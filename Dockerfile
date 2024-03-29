FROM python:3.11
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000", "--verbosity", "2" ]
