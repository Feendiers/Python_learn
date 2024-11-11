# TODO Напишите функцию для поиска индекса товара

def index(list, product):
    # Использую метод enumerate(), который определяет объект и его индекс в массиве
    for i, ite in enumerate(list):
        #Если переданая функцию переменная совпадает с найденной в списке по значению.
        #Возвращаю индекс значения в массиве
        if product == ite:
            return i
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index(items_list, find_item) #Переменная получает значение после работы функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
