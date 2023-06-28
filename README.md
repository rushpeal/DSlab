# LR5 Consul
## Вимоги:
Всі мікросервіси мають реєструватись при старті у Consul, кожного з сервісів може бути запущено декілька екземплярів:
facade-service
logging-service
messages-service

### В цій роботі необxідно задокерувати facade-service, logging-service та messages-service вже були зроблені в минулиx роботаx 
# В корені прописуемо:
```
docker-compose up hz1 hz2 hz3 consul-server consul-client rabbitmq
```
### Після створення контейнерів 
![image](https://github.com/rushpeal/DSlab/assets/47487412/47d2d60c-8b3e-4d2e-a865-8a5920ecd087)

### Вводимо в терміналі  consul-server наступне:
```
consul kv put hazelcast_addrs "hz1:5701,hz2:5701,hz3:5701"
consul kv put map "MAP"
consul kv put queue "DSLR5"
consul kv put rabbit_host "rabbitmq"
```


![image](https://github.com/rushpeal/DSlab/assets/47487412/a2b4247b-3880-4d01-bbab-ac1791b347cb)

 ## Наступним кроком в корені прописуємо:
 ```
docker-compose up --build facade_service logging_service_1 logging_service_2 logging_service_3 messages_service_1 messages_service_2
```
 ### Перевіряємо 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/09ca4051-cf87-4b38-a31e-a8f4a18ca105)

### logging_service
![image](https://github.com/rushpeal/DSlab/assets/47487412/0fc15337-1aa8-40c0-bb9c-132228554853)

### messages_service
![image](https://github.com/rushpeal/DSlab/assets/47487412/df73e6ab-e24a-4186-9b03-2bbbdec79977)

### Лог
![image](https://github.com/rushpeal/DSlab/assets/47487412/4e7c7ca4-0757-4f77-93ed-8f2c4e14a51f)

№ IP-адреси (і порти) мають зчитуватись facade-service з Consul.В коді чи конфігураціях НЕ має бути задано статичних значень адрес.

### Facade
![image](https://github.com/rushpeal/DSlab/assets/47487412/50d0440c-0d84-436c-a56f-8a2b13a19f67)
![image](https://github.com/rushpeal/DSlab/assets/47487412/298f557c-2b27-4331-aac1-9a0a7962a10b)
![image](https://github.com/rushpeal/DSlab/assets/47487412/6c9843ba-3d1b-4869-89ac-80a0c7ea48ae)
 
 ### Logging 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/a375c023-742a-4858-aea8-074f8689f286)

### Message 
![image](https://github.com/rushpeal/DSlab/assets/47487412/093bf76d-669b-4a54-be14-bb92a21c0a09)

# Налаштування для клієнтів Hazelcast мають зберігатись як key/value у Consul і зчитуватись logging-service
Налаштування для Message Queue (адреса, назва черги, …) мають зберігатись як key/value у Consul і зчитуватись facade-service та messages-service

![image](https://github.com/rushpeal/DSlab/assets/47487412/6af452f9-e207-4651-8c6f-a038424386de)

# Надсилаємо POST та GET запити через POSTMAN
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/4c5e86e7-afb6-42e5-bcd4-2c7aa651f8c3)

 ![image](https://github.com/rushpeal/DSlab/assets/47487412/1c82235c-eb24-4780-800d-d728f53e3b84)
![image](https://github.com/rushpeal/DSlab/assets/47487412/7dcf2dad-7b5b-4bcc-996c-8dc733c57151)
![image](https://github.com/rushpeal/DSlab/assets/47487412/f366ba70-8a78-4d27-a220-68048c4a5035)
![image](https://github.com/rushpeal/DSlab/assets/47487412/38c66157-bdaf-4b16-987d-f48bd5f980e2)
![image](https://github.com/rushpeal/DSlab/assets/47487412/63e91cc6-a305-4e23-89eb-0c847ed5c7e5)
![image](https://github.com/rushpeal/DSlab/assets/47487412/a21cc404-6623-4de4-a7ef-7a8a187e5b39)














