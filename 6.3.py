 
def print_matrix(m):
    for row in m:
        print(row)
 
 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
 
# Через zip
transposed = [list(row) for row in zip(*matrix)]
 
print("Исходная матрица:")
print_matrix(matrix)
print("\nТранспонированная матрица:")
print_matrix(transposed)
 
# Прямоугольная матрица 2x3 через генератор списков
rect = [[1, 2, 3], [4, 5, 6]]
rect_t = [[rect[i][j] for i in range(len(rect))] for j in range(len(rect[0]))]
print("\nПрямоугольная матрица 2x3:")
print_matrix(rect)
print("Транспонированная (3x2):")
print_matrix(rect_t)