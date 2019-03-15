FROM python:3.7.2-stretch
MAINTAINER Eric Youngberg <eyoungberg@mapc.org>

ENV QT_GRAPHICSYSTEM "native"

WORKDIR /usr/src/app
VOLUME /tmp/.X11-unix

COPY ./ .
COPY bin/ /opt/bin/

RUN set -ex; \
    \
    apt-get update -qq \
    && apt-get install -y \
      binutils \ 
      build-essential \
      libgl1-mesa-glx \
      libqt5gui5 \
      libx11-xcb1

RUN set -ex; \
    \
    pip3 install -e . \
    && echo "#!/bin/bash \n pip3 install -e . && hpp" > /usr/local/bin/exec-hpp \
    && chmod +x /usr/local/bin/exec-hpp


ENTRYPOINT ["/opt/bin/docker-entrypoint.sh"]
