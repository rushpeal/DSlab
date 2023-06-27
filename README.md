# LR 3
### logging-service працюватиме у підмережі докера, тому міняємо сокети в HazelcastClient з локальної мережі на мережу докера

### Змінна PYTHONUNBUFFERED передається через docker run для корректної роботи потоків stdout та stderr, і відповідно, функції print

## 1. Запустити три екземпляра logging-service (локально їх можна запустити на різних портах), відповідно мають запуститись також три екземпляра Hazelcast
### Переxодимо в папку 
```
logging_service_alt
```
 Далі почергово виконуємо 
 ```
 docker network create hazelcast-network-2

docker build -t logging-service_alt .

docker run -d -p 8011:8001 --env "PYTHONUNBUFFERED=1" --name logserv1 --network hazelcast-network-2 logging-service_alt 

docker run -d -p 8012:8001 --env "PYTHONUNBUFFERED=1" --name logserv2 --network hazelcast-network-2 logging-service_alt 

docker run -d -p 8013:8001 --env "PYTHONUNBUFFERED=1" --name logserv3 --network hazelcast-network-2 logging-service_alt
```
### Додатково створюємо контейнери  кластеру Hazelcast та Hazelcast MC
```
docker run -d --name mem1 --network hazelcast-network-2 -e HZ_CLUSTERNAME=dev -p 5701:5701 hazelcast/hazelcast:latest-snapshot
docker run -d --name mem2 --network hazelcast-network-2 -e HZ_CLUSTERNAME=dev -p 5702:5701 hazelcast/hazelcast:latest-snapshot
docker run -d --name mem3 --network hazelcast-network-2 -e HZ_CLUSTERNAME=dev -p 5703:5701 hazelcast/hazelcast:latest-snapshot
docker run -d --network hazelcast-network-2 -p 8080:8080 hazelcast/management-center:latest-snapshot
```
