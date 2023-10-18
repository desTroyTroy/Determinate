# Accept a matrix of size N x N and take the determinant
def determinant(matrix):
    # If matrix size = 1, make result that element and return
    if len(matrix) == 1:
        result = matrix[0][0]

    else:
        # Initialize a list for tuple pairs
        matrixList = []
        # If matrix size = 2, reach single value and return
        if len(matrix) == 2:
            # Reach single value by appending list with tuple pairs  
            # consisting of the product of the diagonal elements, 
            # later take the difference and return 
            matrixList.append((matrix[0][0] * matrix[1][1], [[1]]))
            matrixList.append((matrix[0][1] * matrix[1][0], [[1]])) 

        else:   
            # If matrix is greater than 2 x 2, calls the minor() function
            # to create the minor matrix for each top row element
            for index in range(len(matrix)):
                matrixList.append((matrix[0][index], minor(matrix, index))) 

        sign = 1    
        result = 0
        # Unpack the tuple pairs into top row element and determinate of the  
        # minor matrix, then take the sumation of the product with alternating signs
        for key, value in matrixList:
            # Recursively call determinate, until a minor 
            # maxtrix of N-1 x N-1 results in a 2 x 2 matrix
            # from which the determinate can reach a single value.
            result += key * determinant(value) * sign
            sign *= -1

    return result

# Create the minor matrix of size N-1 x N-1
def minor(matrix, offset):
    new_matrix = []
    # For each top row element...
    for index in range(1, len(matrix)):
        row = []
        # create a row each with the remainders from       (ex) [ * - - ]
        # the matrix if you exclude the elements in the         [ - a b ]
        # row and column of the current top row element         [ - c d ]
        for i in range(len(matrix)):
            # Excludes element in the same column
            # as the current top row element
            if i != offset:
                row.append(matrix[index][i])
        # Append rows to new matrix that is one 
        # size smaller than the previous matrix
        new_matrix.append(row)
        
    return new_matrix
