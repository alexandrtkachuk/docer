# Version: 0.0.1
FROM ubuntu
EXPOSE 8888

RUN apt-get update

RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y openvpn
RUN apt-get install -y tinyproxy
RUN apt-get install -y net-tools vim
RUN wget 'http://hidemyass.com/vpn-config/vpn-configs.zip'
RUN unzip vpn-configs.zip



#docker run -it  --privileged -p 8888:8888 my:tiny
#с конфига убрать все адреса и прописать чтоб в заголовке не дописывал что это прокси