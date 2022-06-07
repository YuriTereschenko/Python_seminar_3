# Строка содержит набор чисел показать большее и меньшее число. Разделитель пробел

def min_max_in_str(string_of_num):
    arr_of_num = string_of_num.split()
    print(f"Большее число: {max(arr_of_num)}, меньшее число: {min(arr_of_num)}")


num_in_str = "2 4 5 21 0"
min_max_in_str(num_in_str)
