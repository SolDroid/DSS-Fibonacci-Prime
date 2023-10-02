// TO COMPILE: gcc -o fibonacciPrime fibonacciPrime.c -lm

#include <stdio.h>
#include <math.h>
#define MAX_ARR_SIZE 100

// Defining constants for Binet's formula
#define ROOT5 sqrtf(5)
#define PHI (ROOT5+1)/(2)
#define LOGPHI logf(PHI)

unsigned int * find_fibonacci_primes(unsigned int arr[], unsigned int length) {
    return 0;
}

unsigned int fibonacci_index(unsigned int value) {
    unsigned int index, nearFib;
    index = roundf(logf(ROOT5 * value) / LOGPHI);
    nearFib = roundf(powf(PHI, index) / ROOT5)
    return 0;
}

short int is_prime(unsigned int value) {
    // Filters out even numbers
    if (!(value & 1)) return 0;

    // Iterates over possible factors up to and including sqrt(value)
    for (int i = 3; i <= sqrt(value); i++) {
        if (value % i == 0) {
            return 0;
        }
    }
    return 1;
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

    find_fibonacci_primes(arr, arrSize);
    printf("arr[0] = %d", arr[0]);
    return 0;
}