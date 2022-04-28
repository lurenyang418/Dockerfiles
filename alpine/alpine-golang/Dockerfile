FROM lurenyang/alpine

RUN set -eux \
	&& apk add libc6-compat \
	&& wget https://studygolang.com/dl/golang/go1.18.1.linux-amd64.tar.gz \
	&& tar -xf go1.18.1.linux-amd64.tar.gz -C /usr/local/ \
	&& echo "export PATH=/usr/local/go/bin:/go/bin:$PATH" >> /etc/profile \
	&& rm -rf go1.18.1.linux-amd64.tar.gz

ENV ENV=/etc/profile