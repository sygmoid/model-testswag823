FROM ecoron/python36-sklearn

WORKDIR /apps

COPY requirements.txt /apps
RUN apt-get update \
    && pip install -r requirements.txt

COPY *.py /apps/
COPY model.pk /apps/
EXPOSE 3002

CMD ["python", "server.py"]