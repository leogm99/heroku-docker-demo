FROM python:3.9

WORKDIR /demo-temp

COPY ./requirements.txt /demo-temp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /demo-temp/requirements.txt

COPY ./app /demo-temp/app

ENV port=$PORT

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port ${port}"]
