FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /website
COPY requirements.txt /website/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /website/
CMD gunicorn --bind 0.0.0.0:80 website.wsgi