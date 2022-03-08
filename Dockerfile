FROM python:3.11-rc-bullseye

ADD . /Docker_Assgn

RUN pip install bs4

RUN pip install requests

WORKDIR /Docker_Assgn

CMD ["python","Script.py"]