FROM python:3.6.2

COPY . /shiye_data/violet

WORKDIR /shiye_data/violet
RUN pip install -r requirements.txt -i  https://pypi.doubanio.com/simple/
RUN echo "packpage has installed"
EXPOSE 8632

