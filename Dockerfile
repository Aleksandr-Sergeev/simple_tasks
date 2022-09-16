FROM python:3.9
ENV PYTHONUNBUFFERED=1

ENV TZ 'Europe/Moscow'
COPY ./requirements /opt/app/requirements
RUN apt-get update && apt-get install -y cron
RUN pip install -r /opt/app/requirements/python-requirements.txt


COPY . /opt/app/
RUN chmod +x /opt/app/docker-entrypoint.sh
WORKDIR /opt/app/

VOLUME /opt/app/static/
ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]
