// TO COMPILE: gcc -o fibonacciPrime fibonacciPrime.c -lm
// Only includes comments to explain major differences from python version

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX_ARR_SIZE 100

// Defining constants for Binet's formula
#define ROOT5 sqrtl(5)
#define PHI (ROOT5+1)/(2)
#define LOGPHI logl(PHI)

unsigned int fibonacci_index(unsigned int value) {
    unsigned int index, nearFib;
    index = roundl(logl(ROOT5 * value) / LOGPHI);
    nearFib = roundl(powl(PHI, index) / ROOT5);
    if (nearFib == value) {
        return index;
    } else {
        // 0 is only used as default return so unsigned can be used as the return type, an index of 0 would correspond to a value of 0 but this number is filtered out by the basic cases
        return 0;
    }
}

short int is_prime(unsigned int value) {
    if (!(value & 1)) return 0;
    for (unsigned int i = 3; i <= floor(sqrtf(value)); i++) {
        if (value % i == 0) {
            return 0;
        }
    }
    return 1;
}

unsigned int * find_fibonacci_primes(unsigned int arr[], unsigned int length) {
    unsigned int outlength = 0, *outArr = malloc(sizeof(unsigned int) * length);
    for (unsigned int i = 0; i < length; i++) {
        if (arr[i] <= 3) {
            if (arr[i] != 1) {
                outArr[outlength] = arr[i];
                outlength++;
            } else {
                continue;
            }
        }
        unsigned int fibIndex;
        fibIndex = fibonacci_index(arr[i]);
        if (fibIndex == 0) continue;
        if (!is_prime(fibIndex)) continue;
        if (is_prime(arr[i])) {
            outArr[outlength] = arr[i];
            outlength++;
        }
    }
    // 4 is used as the placeholder for the termination of the array in the output as 4 will never be returned otherwise
    outArr[outlength] = 4;
    // Ends the used section of the output array with 0 so that the actual 
    return outArr;
}

int main(void) {
    // Initialise relavant variables
    unsigned int arrSize, arr[MAX_ARR_SIZE];

    // Take array input
    printf("Enter input array size: ");
    scanf("%u", &arrSize);
    printf("Enter values: ");
    for (unsigned int i = 0; i < arrSize; i++) {
        scanf("%u", &arr[i]);
    }

    // Call find_fibonacci_primes function
    unsigned int * fibonacciPrimes = find_fibonacci_primes(arr, arrSize);
    printf("Fibonacci primes: ");
    for (unsigned int i = 0; i < MAX_ARR_SIZE; i++) {
        if (fibonacciPrimes[i] == 4) break; // 4 used as terminator as per find_fibonacci_primes function
        printf("%u, ", fibonacciPrimes[i]);
    }
    printf("\b\b \n");
    return 0;
}