import math


Statistics1 = 0
Statistics2 = 0


def shell_sort_ver1(arr):
    passes = math.floor(math.log(len(arr), 2)) - 1
    while passes >= 0:
        increment = int(pow(2, passes)) - 1
        for start in range(increment, len(arr), 1):
            arr = insertion_sort(arr, start, increment, 1)
        passes -= 1
    return arr


def shell_sort_ver2(arr):
    passes = math.floor(math.log(2 * len(arr) + 1, 3)) - 2
    while passes >= 0:
        increment = int(pow(3, passes)) + int(pow(3, passes - 1))
        for start in range(increment, len(arr), 1):
            arr = insertion_sort(arr, start, increment, 2)
        passes -= 1
    return arr


def insertion_sort(arr, start, gap, version):
    global Statistics1, Statistics2
    new_element = arr[start]
    location = start - gap
    while location >= 0 and arr[location] > new_element:
        if version == 1:
            Statistics1 += 1
        else:
            Statistics2 += 1
        arr[location + gap] = arr[location]
        location -= gap
    arr[location + gap] = new_element
    return arr


test = input()
with open(f'tasks/z5/{test}') as f:
    s = f.readline()
    array = list(map(int, s.split()))
    array_v2 = list(map(int, s.split()))
with open(f'tasks/z5/output0.txt', 'a') as f:
    shell_sort_ver1(array)
    f.write(str(array))
    f.write('\n')
    shell_sort_ver2(array_v2)
    f.write(f'{str(Statistics1)} {str(Statistics2)}')
    f.write('\n')
