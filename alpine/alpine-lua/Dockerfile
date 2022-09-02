FROM lurenyang/alpine-learn

RUN set -eux \
    && apk --no-cache --no-progress update \
    && apk --no-cache --no-progress upgrade \
    && apk add --no-cache --no-progress lua5.4 lua5.4-dev \
    && apk add --no-cache --no-progress --virtual .build-deps build-base unzip \
    && cd /tmp \
    && git clone --depth=1 https://github.com/keplerproject/luarocks.git \
    && cd luarocks \
    && ./configure \
    && make build install \
    && cd \
    && apk del --purge .build-deps \
    && echo -e "#alias \nalias lua=lua5.4\n" >> ~/.bashrc \
    && rm -rf /var/cache/apk/* /tmp/* /root/.cache/*


