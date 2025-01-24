# Importer la b i b l i o t h q u e numpy
import numpy as np

"""
# D f i n i r les matrices A et B
A = np . array ([[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]])
B = np . array ([[9 , 8 , 7] , [6 , 5 , 4] , [3 , 2 , 1]])
print (" Matrice A:")
print ( A )
print ("\ nMatrice B:")
print ( B )
# Addition des matrices
C_add = A + B
print ("\ nAddition des matrices A et B :")
print ( C_add )
# Produit des matrices
C_product = np . dot (A , B )
print ("\ nProduit des matrices A et B :")
print ( C_product )

#-------------------------------------------------------------------------------------------------------


A = np . array ([[2 , 3] , [1 , 4]])

det_A = np . linalg . det ( A )
print ( f" D t e r m i n a n t de A : { det_A }")

if det_A != 0:
    A_inv = np . linalg . inv ( A )
    print (" Inverse de A :")
    print ( A_inv )
else :
    print ("La matrice n’a pas d’inverse , le d t e r m i n a n t est nul.")
"""

#------------------------------------------------------------------------------------------------------
"""
def can_multiply_matrices(A, B):
    
    
    
    Check if two matrices A and B can be multiplied.

    Parameters:
        A (ndarray): The first matrix.
        B (ndarray): The second matrix.

    Returns:
        bool: True if matrices can be multiplied, False otherwise.
    
    
    
    if A.shape[1] == B.shape[0]:
        return True
    else:
        return False



    # Define matrices A and B
A = np.array([[1, 2, 3],
                  [4, 5, 6]])
B = np.array([[7, 8],
                  [9, 10],
                  [11, 12]])

    # Check if multiplication is possible
if can_multiply_matrices(A, B):
        print("Matrices can be multiplied.")
        C = np.dot(A, B)  # Perform multiplication
        print("Resulting matrix:")
        print(C)
else:
        print("Matrices cannot be multiplied. Ensure that the number of columns in A equals the number of rows in B.")
"""

#-----------------------------------------------------------------------------------------------------------------------------



A = np . array ([[2 , 3] , [1 , 4]])

det_A = np . linalg . det ( A )
print ( f" D t e r m i n a n t de A : { det_A }")

if det_A != 0:
    A_inv = np . linalg . inv ( A )
    print (" Inverse de A :")
    print ( A_inv )
else :
    print ("La matrice n’a pas d’inverse , le d t e r m i n a n t est nul.")