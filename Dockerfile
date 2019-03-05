FROM python:3.7.2-stretch
MAINTAINER Eric Youngberg <eyoungberg@mapc.org>

ENV QT_GRAPHICSYSTEM "native"

WORKDIR /usr/src/app
VOLUME /tmp/.X11-unix

COPY ./ .

RUN set -ex; \
    \
    apt-get update -qq \
    && apt-get install -y \
      build-essential \
      libgl1-mesa-glx \
      libx11-xcb1 \
      libqt5gui5

RUN set -ex; \
    \
    pip3 install -e . \
    && echo "#!/bin/bash \n pip3 install -e . && hpp --headless acton boxborough boston waltham" > /usr/local/bin/exec-hpp \
    && chmod +x /usr/local/bin/exec-hpp


CMD ["exec-hpp"]
