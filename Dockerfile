# syntax=docker/dockerfile:1
# we create our IMAGE by this description:
FROM python:3.8
WORKDIR /usr/src/try_celery
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONRUNBUFFERED 1

RUN #apk add --no-cache gcc musl-dev linux-headers
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY try_celery /usr/src/try_celery
CMD ["python", "manage.py", 'runserver', "0.0.0.0:8000"]

# start new img and changing PORTS 8000-8000
# docker run --name try_celery_img -p 8000:8000 -d try_celery