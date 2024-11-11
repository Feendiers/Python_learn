# TODO импортировать необходимые молули
import csv #Добавляю библиотеки для работы с csv и json файлами
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as file:#Открываю csv файл при помощи метода with open()
        arr = []#Создаю перменную-массив в которую буду записывать данные
        #При помощи метода библиотеки csv csv.DictReader() десериализую данные и считываю их построчно в словари, поскольку так работает данный метод
        #затем записываю данные в формате словарей в специально созданную переменную-массив arr
        for data in csv.DictReader(file):
            arr.append(data)

    ...  # TODO Сериализовать в файл с отступами равными 4
    # Для сериализации данных в формате json при помощи метода with создаю json файл с заданным названием
    with open(OUTPUT_FILENAME, "w") as file:
        # Далее при помощи метода json.dump() библиотеки json, используя в качестве аргументов полученный
        # до этого массив словарей, переменную, которая отвечает за созданный файл, а также задаю значение
        # для необязательного параметра indent, который отвечает за отступ и делаю его равным 4
        json.dump(arr, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
