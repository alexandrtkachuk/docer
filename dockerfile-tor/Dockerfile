#
# Quick and easy Tor
#

# todo: use alpine linux to keep our images smaller
FROM bwstitt/debian:jessie

# setup Tor apt source. https://www.torproject.org/docs/debian
# There is no need to set up apt pins: https://trac.torproject.org/projects/tor/ticket/12687
RUN echo "deb http://deb.torproject.org/torproject.org jessie main" >/etc/apt/sources.list.d/tor.list \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 \
 && docker-apt-install \
    deb.torproject.org-keyring \
    lsof \
    tor \
    tor-arm

# add basic configuration for Tor
COPY torrc /etc/tor/torrc
COPY armrc /var/lib/tor/.arm/armrc
RUN chmod 644 /etc/tor/torrc /var/lib/tor/.arm/armrc \
 && chown -R debian-tor:debian-tor /etc/tor /var/lib/tor
VOLUME /var/lib/tor

USER debian-tor
ENTRYPOINT ["/usr/bin/tor"]
CMD ["-f", "/etc/tor/torrc"]

# Rockerfiles have this, but don't work with Docker Hub
# ATTACH /bin/bash -l
# PUSH bwstitt/tor:latest
