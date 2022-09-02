FROM lurenyang/alpine

RUN set -eux \
    && apk --no-cache --no-progress update \
    && apk add --no-cache --no-progress bash bash-completion tree curl ripgrep git vim \
    && rm -rf /var/cache/apk/*

CMD ["/bin/bash"]