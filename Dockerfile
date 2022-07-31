FROM python:3.8
WORKDIR /homework11
COPY src/requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest", "--browser", "chrome"]