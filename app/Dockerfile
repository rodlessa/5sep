FROM python:3.6

WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . /app

RUN apt-get update \
    && apt-get install -y gettext libgettextpo-dev \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]