FROM python:3.6-slim-stretch

ENV PIP_NO_CACHE_DIR 1

# Pypi package Repo upgrade
RUN pip3 install --upgrade pip setuptools

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# Starting Worker
CMD ["python3","-m","botapi"]

EXPOSE 8800