FROM python:3.8-slim-buster

WORKDIR /appl
ENV WERKZEUG_RUN_MAIN=true
COPY service-validate-mail.py /appl

COPY blacklist.conf requirements.txt /appl/

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --upgrade pip  && pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r /appl/requirements.txt 

CMD ["python3","service-validate-mail.py"]