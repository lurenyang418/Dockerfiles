FROM alpine:3.9

LABEL lurenyang <lurenyang@outlook.com>

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV TZ=Asia/Shanghai
ENV MONGO_USERNAME=root
ENV MONGO_PASSWORD=password

RUN set -eux \
  && sed -i s#dl-cdn.alpinelinux.org#mirror.tuna.tsinghua.edu.cn#g /etc/apk/repositories \
  && apk --no-cache --no-progress update \
  && apk --no-cache --no-progress upgrade \
  && apk add --no-cache tzdata ca-certificates \
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
  && echo $TZ > /etc/timezone \
  && apk add --no-cache mongodb \
  && rm -rf /var/cache/apk/*

COPY entrypoint.sh /entrypoint.sh
COPY mongod.conf /etc/mongod.conf

VOLUME /data/db

EXPOSE 27017 28017

ENTRYPOINT ["/entrypoint.sh"]
CMD ["mongod", "--bind_ip_all"]