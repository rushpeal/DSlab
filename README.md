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

### Вводимо в терміналі  
```
consul-server
```

![image](https://github.com/rushpeal/DSlab/assets/47487412/a2b4247b-3880-4d01-bbab-ac1791b347cb)








