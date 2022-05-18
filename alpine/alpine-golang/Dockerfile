FROM lurenyang/alpine-arm64v8

RUN set -eux \
	&& apk add libc6-compat \
	&& wget https://studygolang.com/dl/golang/go1.18.2.linux-arm64.tar.gz \
	&& tar -xf go1.18.2.linux-arm64.tar.gz -C /usr/local/ \
	&& echo "export PATH=/usr/local/go/bin:/go/bin:$PATH" >> /etc/profile \
	&& rm -rf go1.18.2.linux-arm64.tar.gz

ENV ENV=/etc/profile