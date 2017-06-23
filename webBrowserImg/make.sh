docker rmi my:webBrowserImg -f
docker build -t my:webBrowserImg .

#docker run  --memory=512m --memory-swap=128m  -d  -p 5556:5556 my:webBrowserImg sh -c "service tor start; python3 loadImg.py"
