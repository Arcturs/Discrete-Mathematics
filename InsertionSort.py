Statistics = 0


def insertion_sort(array):
    global Statistics
    for i in range(1, len(array), 1):
        # до len(array) не включительно
        new_element = array[i]
        location = i - 1
        while location >= 0 and array[location] > new_element:
            Statistics += 1
            array[location + 1] = array[location]
            location -= 1
        array[location + 1] = new_element
    return array


test = input()
with open(f'tasks/z4/{test}') as f:
    array = list(map(int, f.readline().split()))
with open(f'tasks/z4/output0.txt', 'a') as f:
    array = insertion_sort(array)
    f.write(str(array))
    f.write('\n')
    f.write(str(Statistics))
