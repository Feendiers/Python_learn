list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяю середину изначального массива
middle_index = len(list_players) // 2
# При помощи среза массива создаю 2 новых массива
first_team = list_players[:middle_index]  
second_team = list_players[middle_index:]
# Вывожу новые получившиеся массивы
print(first_team)
print(second_team)
