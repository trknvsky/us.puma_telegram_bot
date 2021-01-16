FROM  python:3.8.2

RUN pip3 install pipenv
RUN mkdir /src
WORKDIR /src
COPY . /src

RUN pipenv install --system --deploy --ignore-pipfile
