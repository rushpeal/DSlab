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

№ Продемонструйте роботу Distributed Map

![image](https://github.com/rushpeal/DSlab/assets/47487412/3b3caac6-2dc7-40bb-a43c-df8b02a3d75a)

![image](https://github.com/rushpeal/DSlab/assets/47487412/249b98c5-935b-49fa-a458-a4cda482da6b)

## Перевіряемо management-center та бачимо нерівномірний розподіл 
![image](https://github.com/rushpeal/DSlab/assets/47487412/7fe2281d-b40b-41eb-8bab-4a6ebcff3dc7)
 
##Відключаемо одну ноду
![image](https://github.com/rushpeal/DSlab/assets/47487412/fca79aad-5e48-48f6-99a0-175bcbb0e2fc)

 ### Перевіряємо цілістність 

 
