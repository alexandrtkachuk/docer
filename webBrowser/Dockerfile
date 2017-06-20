# Version: 0.0.1
FROM zeromq/zeromq
EXPOSE 5555


COPY server.py /server.py

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y curl
RUN apt-get install -y tor
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip3 install selenium
RUN pip3 install lxml
RUN pip3 install zmq
RUN apt-get install -y build-essential python-dev phantomjs npm nodejs 
RUN cp /usr/bin/nodejs /usr/bin/node
RUN npm install -g phantomjs


##need run tor
CMD ["service", "tor", "start"]

#ENTRYPOINT ["tor"]

CMD ["python3", "server.py"]

##easy run: 
##docker run  -d  -p 5551:5555 my:webBrowser sh -c "service tor start; ./server.py"
##or 
##docker run  --memory=512m  -d  -p 5555:5555 my:webBrowser sh -c "service tor start; ./server.py
