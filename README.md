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
## В результаті отримаємо наступне 
![image](https://github.com/rushpeal/DSlab/assets/47487412/dc5dd873-bb1c-4730-9f2b-8f6a76ffb822)

# 2. Через HTTP POST записати 10 повідомлень msg1-msg10 через facade-service
 ### Post запити відправляемо через Postman 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/22358570-ea62-47b1-a625-60ff975f830d)
# 3. Показати які повідомлення отримав кожен з екзмеплярів logging-service 
![image](https://github.com/rushpeal/DSlab/assets/47487412/173d3eef-6f81-4e8b-9805-5e2f43a08aad)
![image](https://github.com/rushpeal/DSlab/assets/47487412/322befd8-e2b0-4afe-9049-2949d052e85a)
![image](https://github.com/rushpeal/DSlab/assets/47487412/5e96f5b1-ba95-408d-8943-703461fbbffa)
### Відповідно інформація відображаеться в мапі 
![image](https://github.com/rushpeal/DSlab/assets/47487412/93dfd739-9b56-4a1d-a19c-4238a669e1e8)

# 4. Через HTTP GET з facade-service прочитати повідомлення
![image](https://github.com/rushpeal/DSlab/assets/47487412/79999887-bc2d-4ddb-bd09-b3f03e947336)
 Також все логуеться 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/5f29e3bb-8d0f-4215-b873-6a3341e0be90)

### Якщо запит дійде до працюючого єкземпляру -отримаємо відповідь 
![image](https://github.com/rushpeal/DSlab/assets/47487412/2c278dd9-70c6-47ac-819e-4a3d8f27b85b)
![image](https://github.com/rushpeal/DSlab/assets/47487412/1eff400c-4542-4bf7-85e8-815938875bca)

### Якщо запит дійде до вимкненого єкземпляру -отримаємо помилку 
![image](https://github.com/rushpeal/DSlab/assets/47487412/9f1bf39b-f6cd-49cd-a0bf-a3d72ee53e98)
![image](https://github.com/rushpeal/DSlab/assets/47487412/b63c2469-4538-452e-995d-6abff6e4ca31)









