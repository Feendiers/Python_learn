# TODO Найдите количество книг, которое можно разместить на дискете
n = 4*25*50*100
maks = n/1024**2
k = 1
while maks <= 1.44:
    maks+=maks
    k+=1
print("Количество книг, помещающихся на дискету:", k)