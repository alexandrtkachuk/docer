# Version: 0.0.1
FROM ubuntu
EXPOSE 5000
COPY hello.py /hello.py

#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app #указывает рабочую дерикторию 

#ONBUILD COPY requirements.txt /usr/src/app/
#ONBUILD RUN pip install --no-cache-dir -r requirements.txt
#ONBUILD COPY . /usr/src/app

#
RUN apt update
RUN apt install -y python
RUN apt-get install -y ssh
RUN apt install -y wget
RUN apt-get install -y php
RUN apt-get install -y vim
RUN wget 'https://bootstrap.pypa.io/get-pip.py'
RUN python get-pip.py
RUN pip install Flask


CMD ["python", "hello.py"]

#sudo docker build -t my/repo .

#sudo docker run -p 8888:5000 my/repo

#delete (rm image force)
#sudo docker rmi my/repo -f
