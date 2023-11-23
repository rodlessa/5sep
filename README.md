
## 5SEP

CRUD para logistica, gravar separadores e exibir os top 5, criado em 30 miutos com Django e Bootstrap, SQLite como DB.

Rodar com docker:

```bash
  git clone https://github.com/rodlessa/5sep.git
  cd 5sep
  docker compose up
```
Sem docker:

```bash
  cd app
  pip install -r requirements.txt
  py manage.py runserver 
```
compose.yml
```bash
services: 
  web: 
    build: app 
    ports: 
      - '8000:8000'
```

Dockerfile

```bash
FROM python:3.6

WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY . /app

RUN apt-get update \
    && apt-get install -y gettext libgettextpo-dev \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
```