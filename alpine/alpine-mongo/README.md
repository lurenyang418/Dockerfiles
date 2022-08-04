# 说明

因为 mongodb 开源协议变更, 较新的 alpine 仓库中不再包含 mongo 数据库， 只能从 [较低版本3.9](https://pkgs.alpinelinux.org/packages?name=mongodb&branch=v3.9) 的源中获取

## 默认环境变量

```shell
MONGO_USERNAME=root
MONGO_PASSWORD=password
```

## 启动服务

```shell
docker run -d --name mongo \
    -e MONGO_USERNAME="your-user" \
    -e MONGO_PASSWORD="your-secret" \
    -v /path/to/data:/data/db \
    -p "27017:27017" \
    lurenyang/alpine-mongo
```