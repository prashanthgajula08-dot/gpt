import numpy as np   

# Create a range of numbers from 1 to 99
print(np.arange(1, 100, 1))

# Reshape a 1D array into a 3x3 matrix
a = np.arange(1, 10, 1)
b = a.reshape(3, 3)
print(b)

# Flatten a 2D array into 1D
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

a = np.array(arr)

print(a.flatten())           # Convert to 1D array
print(np.array(arr).flatten())  
print(a.reshape(-1))         # Another way to convert to 1D

# Create arrays with zeros, ones, and a fixed value
brr = np.zeros((3, 3), dtype=int)
print(brr)

arr = np.ones((5, 5), dtype=float)
print(arr)

arr = np.full((5, 4), 5)
print(arr)

# Generate evenly spaced numbers
print(np.linspace(1, 10, 5))
print(np.linspace(1, 100, 18))

# Transpose of a matrix
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

a = np.array(arr)
print(a.T)

# Arithmetic operations on arrays
arr1 = [[1, 2, 3],
        [4, 5, 6]]

arr2 = [[4, 5, 6],
        [7, 8, 9]]

print(np.add(arr1, arr2))       
print(np.subtract(arr1, arr2))  
print(np.divide(arr1, arr2))    
print(np.multiply(arr1, arr2))  


