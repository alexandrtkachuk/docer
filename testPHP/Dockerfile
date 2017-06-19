# Version: 0.0.1
FROM ubuntu
EXPOSE 5000


#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app #указывает рабочую дерикторию 

#ONBUILD COPY requirements.txt /usr/src/app/
#ONBUILD RUN pip install --no-cache-dir -r requirements.txt
#ONBUILD COPY . /usr/src/app

#
RUN apt-get update
RUN apt-get install -y php
RUN apt-get install -y curl
CMD ["php" , "-S", "0.0.0.0:5000"] ####нужно только так... а не локалхост



#sudo docker build -t my/repo .

#sudo docker run -p 8888:5000 my/repo

#delete (rm image force)
#sudo docker rmi my/repo -f
