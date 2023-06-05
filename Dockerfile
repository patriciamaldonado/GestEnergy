
FROM  python:3.12.0b1-slim

LABEL maintainer="patriimaldonado@gmail.com"

COPY /gestenergy /app/gestenergy

COPY requirements.txt /app

RUN pip install --no-cache-dir -r app/requirements.txt

WORKDIR /app

EXPOSE 5000

CMD gunicorn gestenergy.ge_app:app -b 0.0.0.0:${PORT}
