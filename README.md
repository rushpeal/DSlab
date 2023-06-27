# LR 4

## 1.Запустити три екземпляра logging-service (локально їх можна запустити на різних портах), відповідно мають запуститись також три екземпляра Hazelcast

Папка ```logging_service```

```
docker network create hazelcast-network-4

docker build -t logging-service .

docker run -d -p 8011:8001 -e "PYTHONUNBUFFERED=1" --name log-serv1 --network hazelcast-network-4 logging-service 

docker run -d -p 8012:8011 -e "PYTHONUNBUFFERED=1" --name log-serv2 --network hazelcast-network-4 logging-service

docker run -d -p 8013:8011 -e "PYTHONUNBUFFERED=1" --name log-serv3 --network hazelcast-network-4 logging-service
```

## Вмикаємо контейнери кластеру Hazelcast та Hazelcast MC
```
docker run `
-d `
--network hazelcast-network-4 `
-e HZ_CLUSTERNAME=dev `
-p 5702:5701 hazelcast/hazelcast:latest-snapshot

docker run `
     -d `
     --name 1member `
     --network hazelcast-network-4 `
     -e HZ_CLUSTERNAME=dev `
     -p 5701:5701 hazelcast/hazelcast:latest-snapshot

docker run `
-d ` --name 2member `
--network hazelcast-network-4 `
-e HZ_CLUSTERNAME=dev `
-p 5702:5701 hazelcast/hazelcast:latest-snapshot

docker run `
-d `
--name 3member --network hazelcast-network-1 `
-e HZ_CLUSTERNAME=dev `
-p 5703:5701 hazelcast/hazelcast:latest-snapshot
```
# Запустити два екземпляри messages-service
```
docker run -it  --network hazelcast-network-4 --name rab -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management

docker run -d -p 8011:8001 -e "PYTHONUNBUFFERED=1" --name log-serv1 --network hazelcast-network-4 logging-service
docker run -d -p 8012:8001 -e "PYTHONUNBUFFERED=1" --name log-serv2 --network hazelcast-network-4 logging-service
```

![image](https://github.com/rushpeal/DSlab/assets/47487412/83fe0421-b436-42f7-9c56-2d14ea35f170)

#  Записати 10 повідомлень msg1-msg10 через facade-service











