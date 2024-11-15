from matrix import Matrix

my_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

m = Matrix(data=my_matrix)

print(m.get_items(0, 0))

print(m.get_column(1))