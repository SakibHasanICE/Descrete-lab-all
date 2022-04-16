def matrix_intersection(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    print('Rows=', rows, 'Cols=', cols)
    mat_inter = []
    for i in range(len(mat1)):
        mat_inter.append([mat1[i][j] and mat2[i][j] for j in
                          range(len(mat1[0]))])
        return mat_inter


def matrix_union(mat1, mat2):
    mat_union = []
    for i in range(len(mat1)):
        mat_union.append([mat1[i][j] or mat2[i][j] for j in
                          range(len(mat1[0]))])
    return mat_union


matrix1 = [[1, 0, 1],
           [1, 0, 0],
           [0, 1, 1]]
matrix2 = [[1, 0, 1],
           [0, 1, 1],
           [1, 0, 1]]
print('First Matrix=', matrix1)
print('Second Matrix=', matrix2)
mi = matrix_intersection(matrix1, matrix2)
print('Matrix Intersection', mi)
mu = matrix_union(matrix1, matrix2)
print('Matrix Union', mu)
v = ['p', 'q', 'r']
r1 = []
for i in range(len(mi)):
    for j in range(len(mi[0])):
        if mi[i][j] == 1:
            r1.append((v[i], v[j]))
            print(r1)
r2 = []
for i in range(len(mu)):
    for j in range(len(mu[0])):
        if mu[i][j] == 1:
            r2.append((v[i], v[j]))
print(r2)
