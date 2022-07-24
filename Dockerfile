FROM python:3.8
WORKDIR /homework11
COPY requirements.txt /src
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest", "--browser", "chrome"]