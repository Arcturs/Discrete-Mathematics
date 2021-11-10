Statistics = 0
Max_Statistics = 0
Arrays = list()


def choose_pivot(array, first, last):
    global Statistics
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
        Statistics += 1
    array[low], array[up] = array[up], array[low]
    Statistics += 1
    array[first], array[up] = array[up], array[first]
    Statistics += 1
    return up


def quick_sort(array, first, last):
    global Statistics, Max_Statistics
    if first < last:
        pivot = choose_pivot(array, first, last)
        quick_sort(array, first, pivot - 1)
        quick_sort(array, pivot + 1, last)
    return array


def antylex(array, m):
    global Arrays
    if m == 0:
        new_array = array.copy()
        Arrays.append(new_array)
    for i in range(m):
        antylex(array, m - 1)
        if i < m - 1:
            array[i], array[m - 1] = array[m - 1], array[i]
            reverse(array, m - 1)


def reverse(array, m):
    i, j = 0, m - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1


def get_arrays(length):
    global Statistics, Max_Statistics, Arrays
    array = []
    file_arrays = list()
    for i in range(1, length + 1, 1):
        array.append(i)
    antylex(array, length)
    for j in range(len(Arrays)):
        quick_sort(Arrays[j], 0, length - 1)
        if Statistics > Max_Statistics:
            Max_Statistics = Statistics
            file_arrays.clear()
            file_arrays.append(Arrays[j])
        elif Statistics == Max_Statistics:
            file_arrays.append(Arrays[j])
        Statistics = 0
    return file_arrays


with open('tasks/z6/input.txt') as f:
    s = f.readline()
    s = int(s)
arrays = get_arrays(s)
with open(f'tasks/z6/output0.txt', 'a') as f:
    for i in range(len(arrays)):
        f.write(str(arrays[i]))
        f.write('\n')
