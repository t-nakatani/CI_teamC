FROM python:3.9

COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /work

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:9090" ]