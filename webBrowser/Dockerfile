# Version: 0.0.1
FROM zeromq/zeromq
EXPOSE 5555


COPY server.py /server.py
COPY server2.py /server2.py
COPY getUrl.py  /getUrl.py 



RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y curl
RUN apt-get install -y tor
##install python
RUN apt-get install -y wget
#RUN apt-get install -y checkinstall
#RUN wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
#RUN tar -xvf Python-3.5.1.tgz
#WORKDIR /Python-3.5.1
#RUN ./configure
#RUN make
#RUN checkinstall -y
#WORKDIR /
#RUN apt-get install -y python3-pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN rm get-pip.py
RUN pip3 install selenium
RUN pip3 install lxml
#RUN apt-get install -y python3-lxml
RUN pip3 install zmq 
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
#RUN apt-get install -y nodejs
RUN apt-get install -y build-essential phantomjs nodejs vim
#RUN cp /usr/bin/nodejs /usr/bin/node
#RUN apt-get install -y npm
RUN npm install -g phantomjs
#задаем кодировку для python 
RUN export PYTHONIOENCODING=UTF-8

#RUN export PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.4/dist-packages"


##need run tor
#CMD ["service", "tor", "start"]

#ENTRYPOINT ["tor"]

#CMD ["python3", "server.py"]

##easy run: 
##docker run  -d  -p 5551:5555 my:webBrowser sh -c "service tor start; ./server.py"
##or 
##docker run  --memory=512m  -d  -p 5555:5555 my:webBrowser sh -c "service tor start; ./server.py
#docker run  --memory=512m  -d  -p 5555:5555 my:webBrowser sh -c "service tor start; export PYTHONIOENCODING=UTF-8;python3 server2.py;"
