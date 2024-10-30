# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(str1, str2, sept = ','):
    strarr1 = str1.split(sept)
    strarr2 = str2.split(sept)
    arrall = []
    for i in strarr1:
        for j in strarr2:
            print(i, j)
            if i == j:
                arrall.append(i)
    arrall.sort()
    return arrall
print(find_common_participants(participants_first_group, participants_second_group, "|"))
