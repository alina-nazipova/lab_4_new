# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as cvs_file:  # открываем CSV файл, читаем строки как словари, собираем в список
        cvs_data = [row for row in csv.DictReader(cvs_file)]  # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, "w") as json_file:  # открываем JSON файл, записываем данные с отступами 4 пробела
        json.dump(cvs_data, json_file, indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task() # выполняем конвертацию

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="") # выводим содержимое получившегося JSON файла на печать
