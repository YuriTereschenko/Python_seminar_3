# Создать список от -N до N и найти сумму элементов на позициях, позиции указаны в файле
import random


def file_scan(file):  # Считываем данные из файла и переводим их в список целых чисел
    with open(file, 'r') as pos:
        position = pos.readlines()
    for i in range(0, len(position)):
        position[i] = int(position[i])
    return position


def create_random_array(n, list_of_position):  # Создаем список случайных чисел длинной не меньше максимальной позиции
    array = [random.randint(-n, n) for i in range(0, max(list_of_position))]
    return array


def prod_of_nec_el(position, list_for_count):  # Считаем произведение элементов на заданных позициях
    result = 1
    for i in position:
        result *= list_for_count[i-1]
    return result


nec_pos = file_scan("position.txt")
print(f"Позиции из файла:\n{nec_pos}")
rnd_list = create_random_array(15, nec_pos)
print(f"Список случайных чисел:\n{rnd_list}")
print(f"Сумма элементов на заданных позициях = {prod_of_nec_el(nec_pos, rnd_list)}")
