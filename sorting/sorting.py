def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

    return array

def binary_search(array, element, left, right):

    middle = (right + left) // 2
    if array[middle-1] < element <= array[middle]:
        return middle-1
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)

array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
left = 0
right = int(len(array) - 1)
array = qsort(array, left, right)
print("Отсортированный список по возрастанию: ", array)

try:
    element = int(input("Введите любое число в пределах отсортированного списка: "))
except ValueError:
    print("Введенный элемент не соответствует условиям!")
else:
    if element <= array[0] or element > array[-1]:
        print("Числа нет в пределах отсортированного списка!")
    else:
        print("Номер позиции элемента: ", binary_search(array, element, 0, len(array) - 1))

















