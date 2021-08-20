# Given a matrix of nums any number below a zero or is a zero is haunted.
# TODO: where the value is not-zero add to the total sum
#TODO: Where the num is below a zero do not add it to the total
def matrixElementsSum(matrix):
    columns_with_zero = []
    num1 = 0
    for rowindex in range(len(matrix)):
        for columnindex in range(len(matrix[rowindex])):
            currentnum = matrix[rowindex][columnindex]
            numabove = matrix[rowindex -1][columnindex]
            # if rowindex == 0 and columnindex ==0:
            #     num1 = num1 + currentnum
            if currentnum == 0:
               columns_with_zero.append(columnindex)
            if columnindex in columns_with_zero:
                continue
            else:
                num1 = num1 + currentnum 
    print(num1)
    return num1 



# def matrixElementsSum(matrix):
#     num1 = 0
#     for rowindex in range(len(matrix)):
#         for columnindex in range(len(matrix[rowindex])):
#             currentnum = matrix[rowindex][columnindex]
#             numabove = matrix[rowindex -1][columnindex]
#             numabove1 = matrix[rowindex -2][columnindex]
#             numabove2 = matrix[rowindex -3][columnindex] 
#             if rowindex == 0 and currentnum == 0:
#                 for columnindex in range(len(matrix)):
#                     num1 = num1 - currentnum
#             if rowindex == 0:
#                 num1 = num1 + currentnum
#             if currentnum == 0 or numabove ==0:
#                 continue
#             if len(matrix)>2 and currentnum == 0 or numabove1 ==0:
#                 continue
#             if len(matrix)>3 and currentnum == 0 or numabove2 ==0: 
#                 continue
#             else:
#                 num1 = num1 + currentnum 
#     print(num1)
#     return num1 




matrix1 = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 1]]
matrix2 =[[0,1,1,2], 
          [0,5,0,0], 
          [2,0,3,3]]
matrix3 =[[1,1,1], 
 [2,2,2], 
 [3,3,3]]
matrixSolution = 10

matrix4=[[1,1,1,0], 
 [0,5,0,1], 
 [2,1,3,10]]
matrixElementsSum(matrix4)