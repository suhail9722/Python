
#1st Approach
# List to store the results
#result = []
# Loop through the range
#for number in range(2000, 2101):
    # Check if the number is divisible by 7 but not a multiple of 5
#    if number % 7 == 0 and number % 5 != 0:
#        result.append(str(number))
# Join the numbers with a comma and print them
#print(",".join(result))
#print(result)

#2nd Approach

#result = [str(i) for i in range(2000,2100) if i % 7 ==0 and i % 5 !=0]

#3rd Approach using numpy

import numpy as np

# Using NumPy to create an array and filter
numbers = np.arange(2000, 2101)
result = numbers[(numbers % 7 == 0) & (numbers % 5 != 0)]

# Join the numbers with a comma and print them
print(",".join(map(str, result)))

#4rd Approach using pandas

import pandas as pd

# Using NumPy to create an array and filter
numbers = pd.Series(2000, 2100)
result = numbers[(numbers % 7 == 0) & (numbers % 5 != 0)]

# Join the numbers with a comma and print them
print(",".join(map(str, result)))

