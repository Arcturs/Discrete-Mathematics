import math
import sys
W = 5


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def partition(array, first, last):
    p_value = array[first + 1]
    low = first + 1
    up = last
    array[low], array[up] = array[up], array[low]
    while low < up:
        while array[up] > p_value:
            up -= 1
        while array[low] < p_value:
            low += 1
        array[low], array[up] = array[up], array[low]
    array[low], array[up] = array[up], array[low]
    array[first], array[up] = array[up], array[first]
    return up


def select_part(array, k):
    left, right = 0, len(array)
    array.append(sys.maxsize)
    while True:
        v = partition(array, left, right)
        if k < v:
            right = v - 1
        elif k == v:
            return v
        else:
            left = v + 1


def insertion_sort(array, left, right):
    for i in range(left, right + 1, 1):
        new_element = array[i]
        location = i - 1
        while location >= 0 and array[location] > new_element:
            array[location + 1] = array[location]
            location -= 1
        array[location + 1] = new_element
    return array


def select_opt(array, k, left, right):
    while True:
        d = right - left
        if d <= W:
            array = insertion_sort(array, left, right)
            return left + k
        dd = int(math.floor(d / W))
        for i in range(1, dd + 1, 1):
            array = insertion_sort(array, left + W * (i - 1), left + i * W - 1)
            swap(array, left + i - 1, left + W * (i - 1) + int(math.ceil(W / 2)) - 1)
            # левый элемент изначального массива + номер i-го массива
            # левый элемент изначального массива + левый элемент i-го массива + номер места середины массива из w элементов
        v = select_opt(array, int(math.ceil(dd / 2)), left, left + dd - 1)
        array[left], array[v] = array[v], array[left]  # чтобы не создавать вспомогательный массив
        v = partition(array, left, right)
        temp = v - left
        if k > temp:
            k -= temp
            left = v + 1
        elif k == temp:
            return v
        else:
            right = v - 1


with open('input.txt') as f:
    k = f.readline()
    k = int(k)
    array = list(map(int, f.readline().split()))
with open('output.txt', 'a') as f:
    f.write(str(select_part(array, k)))
    f.write('\n')
    f.write(str(select_opt(array, k, 0, len(array) - 1)))
