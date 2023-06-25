# В рамкаx роботи було створено три сервіси
```
facade-service
logging-service
message-service
```
Взаємодія на основі HTTP протоколу згідно завдання
```
facade-service працює на порті 10000
logging-service працює на порті 20000 
message-service працює на порті 30000
```

# Приклад Роботи
## Перше повідомлення
![photo_2023-06-25_12-41-55](https://github.com/rushpeal/DSlab/assets/47487412/aaeacf8b-19a4-4dd3-a5ae-4ec0e1ed1f49)

## Друге повідомлення 
![photo_2023-06-25_12-42-51](https://github.com/rushpeal/DSlab/assets/47487412/9d9d7068-e015-47df-a764-5e43316eadc9)

## Get запит
![photo_2023-06-25_12-43-33](https://github.com/rushpeal/DSlab/assets/47487412/47473ef8-f144-470e-87c1-12668d793d5e)

### logging-service logs
```
[logging-service][App][2023-06-25 12:27:36,527]: Initialized logging for logging-service
[logging-service][App][2023-06-25 12:27:37,377]: Starting httpd at ('', 20000)
[logging-service][Domain][2023-06-25 12:27:48,611]: POST request, message "This is the firts message!" logged with ID "8cc50ce9-133a-11ee-8a2e-7085c22ec7c9"
127.0.0.1 - - [25/Jun/2023 12:27:48] "POST / HTTP/1.1" 200 -
[logging-service][Domain][2023-06-25 12:28:14,649]: POST request, message "This is the second message!" logged with ID "9c4d1a06-133a-11ee-837e-7085c22ec7c9"
127.0.0.1 - - [25/Jun/2023 12:28:14] "POST / HTTP/1.1" 200 -
[logging-service][Domain][2023-06-25 12:28:51,805]: POST request 2 messages sent
127.0.0.1 - - [25/Jun/2023 12:28:51] "GET / HTTP/1.1" 200 -
```

### facade-service logs
```
[facade-service][App][2023-06-25 12:27:33,292]: Initialized logging for facade-service
[facade-service][App][2023-06-25 12:27:34,142]: Starting httpd at ('', 10000)
[facade-service][Domain][2023-06-25 12:27:48,580]: POST request! With new message: This is the firts message!
127.0.0.1 - - [25/Jun/2023 12:27:48] "POST / HTTP/1.1" 200 -
[facade-service][Domain][2023-06-25 12:27:48,636]: Message writen with {'ID': '8cc50ce9-133a-11ee-8a2e-7085c22ec7c9'}
[facade-service][Domain][2023-06-25 12:28:14,639]: POST request! With new message: This is the second message!
127.0.0.1 - - [25/Jun/2023 12:28:14] "POST / HTTP/1.1" 200 -
[facade-service][Domain][2023-06-25 12:28:14,663]: Message writen with {'ID': '9c4d1a06-133a-11ee-837e-7085c22ec7c9'}
[facade-service][Domain][2023-06-25 12:28:51,793]: GET request!
127.0.0.1 - - [25/Jun/2023 12:28:51] "GET / HTTP/1.1" 200 -
```

### message-service logs
```
[message-service][App][2023-06-25 12:27:41,175]: Initialized logging for message-service
[message-service][App][2023-06-25 12:27:42,022]: Starting httpd at ('', 30000)
[message-service][Domain][2023-06-25 12:27:48,631]: POST request
127.0.0.1 - - [25/Jun/2023 12:27:48] "POST / HTTP/1.1" 200 -
[message-service][Domain][2023-06-25 12:28:14,660]: POST request
127.0.0.1 - - [25/Jun/2023 12:28:14] "POST / HTTP/1.1" 200 -
[message-service][Domain][2023-06-25 12:28:51,818]: GET request
127.0.0.1 - - [25/Jun/2023 12:28:51] "GET / HTTP/1.1" 200 -
```
