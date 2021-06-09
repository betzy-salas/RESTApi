FROM ubuntu:latest
RUN echo Updating existing packages, installing and upgrading python and pip.
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install --upgrade pip
RUN echo Copying the myAppServiceJwt Service Flask service into a service directory.
COPY ./ /ServiceJwt
WORKDIR /ServiceJwt
RUN echo Installing Python packages listed in requirements.txt
RUN pip3 install -r requirements.txt
RUN echo Starting python and starting the Flask service...
ENTRYPOINT ["python3"]
CMD ["ServiceJwt.py"]