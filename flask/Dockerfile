# Version: 0.0.1
FROM python:alpine
EXPOSE 5000
COPY hello.py /hello.py

#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app #указывает рабочую дерикторию 

#ONBUILD COPY requirements.txt /usr/src/app/
#ONBUILD RUN pip install --no-cache-dir -r requirements.txt
#ONBUILD COPY . /usr/src/app

#
RUN pip install Flask

CMD ["python", "hello.py"]

#sudo docker build -t my/repo .

#sudo docker run -p 8888:5000 my/repo

#delete (rm image force)
#sudo docker rmi my/repo -f
