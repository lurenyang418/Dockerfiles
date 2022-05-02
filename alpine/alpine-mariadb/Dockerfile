FROM lurenyang/alpine

RUN apk add --no-cache mariadb mariadb-server-utils \
    && rm -f /var/cache/apk/*

ADD docker-entrypoint.sh /scripts/docker-entrypoint.sh
RUN chmod -R 755 /scripts

EXPOSE 3306

VOLUME ["/var/lib/mysql"]

ENTRYPOINT ["/scripts/docker-entrypoint.sh"]
