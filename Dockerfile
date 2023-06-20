FROM python:3.7.17-bookworm
LABEL Eric Youngberg <eyoungberg@mapc.org>

WORKDIR /usr/src/app
VOLUME /usr/src/app

COPY ./ .

RUN set -ex; \
    \
    pip3 install --upgrade pip \
    && pip3 install -e . \
    && echo "#!/bin/bash \n pip3 install -e . && hpp"> /usr/local/bin/exec-hpp \
    && chmod +x /usr/local/bin/exec-hpp

CMD ["exec-hpp"]
