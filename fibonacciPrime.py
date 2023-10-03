# RUN WITH PYTHON 3

# FULL GITHUB REPO AT https://github.com/SolDroid/DSS-Fibonacci-Prime, 
# please visit this to see the full project

import numpy
import time

# Defining constants for Binet's formula
ROOT5 = numpy.sqrt(5)
PHI = (1+ROOT5) / 2
LOGPHI = numpy.log(PHI)

def find_fibonacci_primes(arr):
    outArr = []
    for value in arr:
        # Check for basic cases (README section 2.1)
        if (value <= 3): 
            if(value != 1):
                outArr.append(value)
            else:
                continue

        # Find Fibonacci index (README section 2.2)
        fibIndex = fibonacci_index(value)

        # Skip value if it doesn't have a valid Fibonacci index (not a Fibonacci number) (README section 2.2)
        if (fibIndex == -1): continue

        # Checks if the index is a prime number as all prime Fibonacci numbers will have a prime index, skips the value if not (README section 2.3)
        if (not is_prime(fibIndex)): continue

        # Finally, checks if the value is prime (README section 2.4)
        if (is_prime(value)): outArr.append(value)
    return outArr

def fibonacci_index(value):
    # Find the index of the nearest Fibonacci number using the inverse of an approximation of Binet's formula (README section 2.2)
    index = int(numpy.round(numpy.log(ROOT5 * value) / LOGPHI))
    nearFib = int(numpy.round(numpy.power(PHI, index) / ROOT5))

    # Return the index if it corresponds to the actual input value, otherwise return -1
    if (nearFib == value):
        return index
    return -1

def is_prime(value):
    # Very basic but still has a big o of O(sqrt(n)), this should be sufficient for this application (README section 2.4)
    if (not value & 1): return False

    # Iterate through possible factors, limited to the square root of the value as dividing by any number less than this would result in a corresponding factor greater than sqrt(value)
    for i in range(4, int(numpy.sqrt(value)) + 1):
        if (value % i == 0):
            return False
    return True

# For basic testing of find_fibonacci_primes(arr)
while True:
    arr = input("Enter input list with desired separator(s) (enter E to exit): ")
    try:
        if (arr.upper() == "E"): break
        arr = [int(value) for value in arr.split(" ")]
    except:
        print("Bad Input")
        continue
    start_time = time.time()
    print("Fibonacci primes: ")
    print(find_fibonacci_primes(arr))
    print("Finished in " + str(time.time() - start_time))

# Just a little CubeSat
print("""           Thank
            you

       ____________
      |\___________\\
      |_\___________\\
      |\ |         \ |
      |\\\\|__________\|
      |\\\\|__________\|
      | \|__________\|
      |__|_________| |
      |\ | \   \   \ |
      |_\|__\___\___\|   ______________________
      |\ |         \ |\\ /                      \\
      |\\\\|__________\| |  REMOVE BEFORE FLIGHT |
      |_\|__________\|/ \______________________/
      '\ |         \ |
        \|__________\|
         '           '

           Solomon
           Killam""")