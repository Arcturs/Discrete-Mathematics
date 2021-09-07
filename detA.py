def create_matrix(m, array):
    new_matrix = [[0] * (len(array) - 1) for _ in range(len(array) - 1)]
    m %= len(array)
    k1, j1 = 0, 0
    for k in range(len(array)):
        if k != 0:
            for j in range(len(array[k])):
                if j != m:
                    new_matrix[k1][j1] = array[k][j]
                    j1 += 1
            k1 += 1
            j1 = 0
    return new_matrix


def find_det(array):
    det = 0
    if len(array) == 2:
        return array[0][0] * array[1][1] - array[0][1] * array[1][0]
    else:
        for k in range(len(array)):
            el = array[0][k]
            det += pow(-1, k) * el * find_det(create_matrix(k, array))
    return det


test = input()
matrix = []
with open(f'tasks/z1/inputs/{test}') as f:
    for line in f:
        matrix.append(list(map(int, line.split())))
with open('output.txt', 'w') as w:
    w.write(str(find_det(matrix)))
