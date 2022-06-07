# Дано число. Составьте список чисел Фибоначи, в том числе для отрицательных индексов

def fib_arr(n):
    result = [-1, 1, 0, 1, 1]
    for i in range(0, n - 2):
        result.insert(0, (result[1] - result[0]))
    for j in range(0, n - 2):
        result.append(result[len(result)-1]+result[len(result)-2])

    return result


print(fib_arr(100))
