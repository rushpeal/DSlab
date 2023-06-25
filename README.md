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
 
##Відключаемо одну ноду
![image](https://github.com/rushpeal/DSlab/assets/47487412/fca79aad-5e48-48f6-99a0-175bcbb0e2fc)

 ### Перевіряємо цілістність 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/c31626d6-0805-4cb6-8273-ce3f637225f9)

 №№ Выдкидаэмо дві ноди 
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/a654b1b1-e351-480c-82ed-02b94af58495)

 №№№ Перевіряемо цілісність
 ![image](https://github.com/rushpeal/DSlab/assets/47487412/c32fa05e-d7c7-49e0-903f-06ef9b0b24c8)

 В результаті перевірки (навіть без перевірки бачимо що частина даниx втрачена при вимкненій ноді)
 




 
