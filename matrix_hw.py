n = int(input())

matrix = []

for i in range(n):
    row = input()
    matrix.append(row)  

search_char = input()  

found = False 
for row in range(n):
    for col in range(len(matrix[row])):
        if matrix[row][col] == search_char:
            print(f"({row}, {col})")
            found = True
            break

if not found:
    print(f"{search_char} does not exist in matrix!")

  
# matrix = []
# row_col = int(input())

# for row in range(row_col):
#     matrix.append([])
#     for col in range(row_col):
#         matrix[row].append(col + 1 + row * row_col)
# print(*matrix, sep='\n')

# matrix = []
# row_col = int(input())

# for row in range(row_col):
#     matrix.append([])
#     for col in range(row_col):
#         matrix[row].append(col + 1 + row * row_col)

# flattened_matrix = [element for row in matrix for element in row]
# print(flattened_matrix)



# matrix = []
# rows_cols = int(input())

# for row in range(rows_cols):
#     matrix.append([])
#     for col in range(rows_cols):
#         matrix[row].append(col + 1 + row * rows_cols)

# for row in matrix:
#     row_sum = sum(row)
#     print(row_sum)





# n = int(input())
# matrix = []

# for _ in range(n):
#     row = list(map(int, input().split(', ')))
#     matrix.append(row)

# diagonal_sum = sum(matrix[i][i] for i in range(n))
# print(diagonal_sum)
