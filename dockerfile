FROM python:3.13.1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "filmreviewer/manage.py", "runserver", "0.0.0.0:8000"]
