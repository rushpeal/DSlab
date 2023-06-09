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
docker build -t message-service  .
docker run -d -p 8021:8021 -e "PYTHONUNBUFFERED=1" --name msg-serv1 --network hazelcast-network-4 message-service  
docker run -d -p 8022:8021 -e "PYTHONUNBUFFERED=1" --name msg-serv2 --network hazelcast-network-4 message-service
```

![image](https://github.com/rushpeal/DSlab/assets/47487412/83fe0421-b436-42f7-9c56-2d14ea35f170)

#  Записати 10 повідомлень msg1-msg10 через facade-service

### Запис робиться за допомогою postman 
![image](https://github.com/rushpeal/DSlab/assets/47487412/270b64f8-5163-49e2-8fa2-6ba797d42310)

### facade-service logs
![image](https://github.com/rushpeal/DSlab/assets/47487412/e38fb944-c67f-4cbd-ac83-5d0fee388155)

 ### Повідомлення які отримав кожен з екземплярів logging-service
 Повідомленя можна бачити в логаx 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/c4f2409e-97e5-4b5d-ac75-b153cabc9efa)
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/ffe10fc8-efa8-4a51-a54c-6b3344489447)
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/1d804b59-c622-45e8-8180-199691169c35)
### Відповідно, активінсть відображаеться на мапі (Велика кільість даниx отрималась в результаті довгиx перевірок)
![image](https://github.com/rushpeal/DSlab/assets/47487412/c108c4cb-d685-4fd4-9ccf-bd2578f4a572)

## Показати які повідомлення отримав кожен з екземплярів messages-service
![image](https://github.com/rushpeal/DSlab/assets/47487412/b98ca98e-752d-4320-b92f-4d91acc10dec)

![image](https://github.com/rushpeal/DSlab/assets/47487412/2e04240c-6e0d-47c3-a433-a0fb1fceabc8)
## Rabbitmq
![image](https://github.com/rushpeal/DSlab/assets/47487412/2df6d914-e9e6-4e3a-ac4a-6827b1d94771)

# Декілька разів викликати HTTP GET на facade-service та отримати об'єднані дві множини повідомлень - це мають бути повідомлення з logging-service та messages-service:
Як видно на скріншоті - в результаті GET запиту виводяться усі занесенні данні 
![image](https://github.com/rushpeal/DSlab/assets/47487412/049d971c-0888-4966-ab89-d24c22d329ef)














