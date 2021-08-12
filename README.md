# rj

## 创建数据库迁移

```shell
alembic revision --autogenerate -m "Added initial table"
```

## 应用数据库迁移

```shell
alembic upgrade head
```
