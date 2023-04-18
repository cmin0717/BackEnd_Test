FROM python:3.10

WORKDIR /payhere

COPY ./requirements.txt /payhere/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /payhere/requirements.txt
 
COPY ./app /payhere/app
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]