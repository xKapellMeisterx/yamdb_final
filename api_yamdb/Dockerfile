FROM python:3.7-slim

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]