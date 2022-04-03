# Dockerfiles
基础 Docker 镜像

1. 基于官方镜像, 添加中文支持和时区设置

```shell
docker build -f Dockerfile.base -t minipuppy/ubuntu18 .
```

2. 基于 base 镜像, 加入 gcc/g++ (默认版本 7)
```shell
docker build -f Dockerfile.gcc -t minipuppy/ubuntu18_gcc7 .
```

3. 基于 gcc 镜像, 新增 Python (默认版本 3.6)
```shell
docker build -f Dockerfile.py -t minipuppy/ubuntu18_gcc7_py36 .
```