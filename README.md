#LAB 2 
Я скачав та встановив докер контейнери  hazelcast та management-center
Створуемо віртуальну мережу 
'''
PS D:\DS-labs-lab2> docker network rm hazelcast-network
hazelcast-network
'''

## Створюемо 3 контейнери  з одного кластеру  і додатково контейнер management
![image](https://github.com/rushpeal/DSlab/assets/47487412/62221a2d-7665-4708-b464-8102e792c856)

## Перевіряємо management-center і бачимо шо все працює

![image](https://github.com/rushpeal/DSlab/assets/47487412/cf30520c-b86a-4183-9040-f14cd8be66f2)

## Продемонструйте роботу Distributed Map

![image](https://github.com/rushpeal/DSlab/assets/47487412/3b3caac6-2dc7-40bb-a43c-df8b02a3d75a)

![image](https://github.com/rushpeal/DSlab/assets/47487412/249b98c5-935b-49fa-a458-a4cda482da6b)

## Перевіряемо management-center та бачимо нерівномірний розподіл 
![image](https://github.com/rushpeal/DSlab/assets/47487412/7fe2281d-b40b-41eb-8bab-4a6ebcff3dc7)
 
## Відключаемо одну ноду
![image](https://github.com/rushpeal/DSlab/assets/47487412/fca79aad-5e48-48f6-99a0-175bcbb0e2fc)

 ### Перевіряємо цілістність 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/c31626d6-0805-4cb6-8273-ce3f637225f9)

 ### Відкидаємо дві ноди 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/a654b1b1-e351-480c-82ed-02b94af58495)

 ### Перевіряемо цілісність
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/c32fa05e-d7c7-49e0-903f-06ef9b0b24c8)

 В результаті перевірки (навіть без перевірки бачимо що частина даниx втрачена при вимкненій ноді)

 # Змінити backup-count 
 ## Змінимо значення на 0 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/f5e60f7f-c32b-48d8-8e0a-ba3d16560c84)

### Після зміни значення backup-count  значно змінилася швидкість запису виросла у рази

![image](https://github.com/rushpeal/DSlab/assets/47487412/39f532ff-abe1-4f49-8f09-658d905e90b6)

### Але після зміни налаштувать отримали втрати 
![image](https://github.com/rushpeal/DSlab/assets/47487412/7bcc6cbb-05d0-42dd-88b1-102df9bdf4fb)

### Вимкнули дві ноди
![image](https://github.com/rushpeal/DSlab/assets/47487412/b45de756-3b65-46cf-b4a4-3298c3861498)

## б) 2
![image](https://github.com/rushpeal/DSlab/assets/47487412/ccec2b95-f75f-440d-a00a-5b8a9b7218e3)

### Через великий час завантаження даниx довелось зменшити кількість запитів
![image](https://github.com/rushpeal/DSlab/assets/47487412/43f734c6-a7d0-4219-8baa-c7fd878d14bb)

### Вимикаємо першу ноду 
![image](https://github.com/rushpeal/DSlab/assets/47487412/e93067cf-1891-48f9-a9ef-7c644de9c195)

### Вимикаємо дві ноди 
![image](https://github.com/rushpeal/DSlab/assets/47487412/ec41c1a9-c992-461f-992a-195e89da56de)
# Продемонструйте роботу Distributed map with locks.
## Після запуску  бачимо що результати очікувано інкримінуються
![image](https://github.com/rushpeal/DSlab/assets/47487412/8fe1dd12-b6af-4aa8-b1b3-0b051a88bacc)

![image](https://github.com/rushpeal/DSlab/assets/47487412/3cd08c85-55c5-4f9f-9c42-1dc0a69b58bd)










 
