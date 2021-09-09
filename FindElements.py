Statistics = 0


def sequential_search(array, target):
    global Statistics
    for i in range(len(array)):
        Statistics += 1
        if target == array[i]:
            return i
    return 0


def binary_search(array, target):
    global Statistics
    start, end = 1, len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        Statistics += 1
        if array[middle] > target:
            end = middle - 1
        else:
            if array[middle] == target:
                return middle
            else:
                start = middle + 1
    return 0


def interpolation_search(array, target):
    global Statistics
    left, right = 0, len(array) - 1
    while left <= right:
        Statistics += 1
        next = left + (right - left) * (target - array[left]) // (array[right] - array[left])
        if array[next] > target:
            left = next + 1
        else:
            if array[next] == target:
                return next
            else:
                right = next - 1
    return 0


def count_statistics(array):
    global Statistics
    i_s, b_s, s_s = 0, 0, 0
    for i in range(len(array)):
        sequential_search(array, array[i])
        s_s += Statistics
        Statistics = 0
        binary_search(array, array[i])
        b_s += Statistics
        Statistics = 0
        interpolation_search(array, array[i])
        i_s += Statistics
        Statistics = 0
    return [s_s / len(array), b_s / len(array), i_s / len(array)]


test = input()
array = []
with open(f'tasks/z3/{test}') as f:
    array = list(map(int, f.readline().split()))
with open(f'tasks/z3/output0.txt', 'a') as f:
    lst = count_statistics(array)
    f.write(f'Последовательный поиск: {lst[0]} \n')
    f.write(f'Двоичный поиск: {lst[1]} \n')
    f.write(f'Интерполяционный поиск: {lst[2]} \n')
