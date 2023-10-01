import numpy
import time

ROOT5 = numpy.sqrt(5)
PHI = (1+ROOT5) / 2
LOGPHI = numpy.log(PHI)

total_time = 0
iters = 1000

def find_fibonacci_primes(arr):
    outArr = []
    for value in arr:
        # Check for basic cases
        if (value == 1): continue
        if (value <= 3): outArr.append(value)

        # Find Fibonacci index
        fibIndex = fibonacci_index(value)

        # Skip value if it doesn't have a valid Fibonacci index (not a Fibonacci number)
        if (fibIndex == -1): continue

        # Checks if the index is a prime number as all prime Fibonacci numbers will have a prime index, skips the value if not
        # How this logic was derived can be found here, alongside the rationale for the added is_prime() usage
        if (not is_prime(fibIndex)): continue

        # Finally, checks if the value is prime
        if (is_prime(value)): outArr.append(value)
    return outArr

def fibonacci_index(value):
    # Find the index of the nearest Fibonacci number using the inverse of an approximation of Binet's formula
    # How this logic was derived can be found here
    index = int(numpy.round(numpy.log(ROOT5 * value) / LOGPHI))
    nearFib = int(numpy.round(numpy.power(PHI, index) / ROOT5))

    # Return the index if it corresponds to the actual input value, otherwise return -1
    if (nearFib == value):
        return index
    return -1

def is_prime(value):
    # Very basic but still has a big o of O(sqrt(n)), this should be sufficient for this application
    if (not value & 1): return False

    # Iterate through possible factors, limited to the square root of the value as dividing by any number less than this would result in a corresponding factor greater than sqrt(value)
    for i in range(2, int(numpy.sqrt(value))):
        if value % i == 0:
            return False
    return True

# for j in range(iters):
#     start_time = time.time()
#     find_fibonacci_primes([2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 10008, 1213190, 1231231, 91247])
#     # print(is_prime(1000000015787))
#     # print("--- " + str(time.time() - start_time) + " seconds ---")
#     total_time += time.time() - start_time

while True:
    arr = input("Enter input list with desired separator(s) (enter E to exit): ")
    if (arr.upper() == "E"): break
    try:
        arr = [int(value) for value in arr.split(" ")]
    except:
        print("Bad Input")
        continue
    start_time = time.time()
    print(find_fibonacci_primes(arr))
    print("Finished in " + str(time.time() - start_time))

print("""     Thank
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