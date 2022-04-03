FROM minipuppy/ubuntu18_gcc7


# 源内包含 3.6(默认), 3.7, 3.8
ENV PY_VERSION=3.6

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
    && apt install -y wget python3 python3-distutils \
    && wget -q --no-cache --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && rm -rf get-pip.py \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
