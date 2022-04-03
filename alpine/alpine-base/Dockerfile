FROM alpine

LABEL lurenyang <lurenyang@outlook.com>

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV TZ=Asia/Shanghai

RUN set -eux \
    && sed -i s#dl-cdn.alpinelinux.org#mirror.tuna.tsinghua.edu.cn#g /etc/apk/repositories \
    && apk --no-cache --no-progress update \
    && apk --no-cache --no-progress upgrade \
    && apk add --no-cache tzdata ca-certificates \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && rm -rf /var/cache/apk/*
