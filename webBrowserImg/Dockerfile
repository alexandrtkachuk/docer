# Version: 0.0.1
FROM my:webBrowser 
EXPOSE 5556


COPY loadImg.py /loadImg.py

# remove current pycurl
#RUN pip remove pycurl

# set PYCURL_SSL_LIBRARY
#export PYCURL_SSL_LIBRARY=nss
RUN apt-get install -y python3-pycurl
# recompile and install pycurl
#RUN pip3 install pycurl
#RUN pip3 install pycurl

##easy run: 
##docker run  --memory=512m --memory-swap=128m  -d  -p 5556:5556 my:webBrowserImg sh -c "service tor start; python3 loadImg.py"
