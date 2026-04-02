# TODO решите задачу
import json  # импортируем библиотеку
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f: # открываем файл с исходными данными
        dataset = json.load(f) # преобразуем json строку в структуру данных python
    total_weighted_sum = 0.0 # счетчик суммы

    for element in dataset: # обходим все элементы
        score_value = element.get('score', 0) # достаем значение оценки (если отсутствует - берем 0)
        weight_value = element.get('weight', 0) # достаем значение веса (если отсутствует - берем 0)
        multiplication_result = score_value * weight_value # считаем произведение текущей пары
        total_weighted_sum += multiplication_result # накапливаем промежуточный итог

    rounded_output = round(total_weighted_sum, 3) # устанавливаем нужную точность округления
    return rounded_output # возвращаем итоговое значение
print(task()) # печатаем
