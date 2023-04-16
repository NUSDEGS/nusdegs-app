FROM python:3.11
WORKDIR /app
COPY . .
RUN python -m venv venv && . venv/bin/activate
RUN pip install -r requirements.txt
RUN python manage.py migrate
CMD [ "./venv/bin/python", "manage.py", "runserver" ]
