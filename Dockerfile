FROM python:3.6.2

COPY . /project/api_project

WORKDIR /project/api_project
RUN pip install -r requirements.txt -i  https://pypi.doubanio.com/simple/
RUN echo "packpage has installed"
EXPOSE 8632

