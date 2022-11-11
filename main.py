import random
import storage
l=random.randint(1,1000000)
b=str(l)
d=input('Введите никнейм')
s=storage.create_user(d,b)
#я ацтек