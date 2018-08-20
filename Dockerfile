FROM python:3.5

WORKDIR /stagirovka

ADD . /stagirovka

EXPOSE 8000

RUN pip install -r /stagirovka/requirements.txt

RUN python /stagirovka/manage.py test

CMD ["python", "/stagirovka/manage.py", "runserver", "0.0.0.0:8000"]