def get_matrix(n, m, value):
    elm = []
    matrix = []
    k = 0  # флаг внутреннего цикла
    if k == 0:
        for i in range(n):
            matrix.append(elm)
        for j in range(m):
            elm.append(value)
            k += 1
    return matrix


result1 = get_matrix(2,2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
