# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(str1, str2, sept = ','):
    # Преобразую строковые объекты в множества
    arr1 = set(str1.split(sept))
    arr2 = set(str2.split(sept))
    total = arr1 & arr2#Определение общих элементов
    #Проверяю есть ли общие элементы и если есть, то
    #преобразую множество в список, затем сортирую его
    #по возрастанию и возвращаю отсортированный список с
    #общими элементами у двух изначальных строк
    if total:
        final = list(total)
        final.sort()
        return final
#Проверяю работу функции, функция в качестве аргументов принимает две строки и разделитель для них
print(find_common_participants(participants_first_group, participants_second_group, "|"))
