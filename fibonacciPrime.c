#include <stdio.h>
#include <math.h>
#define MAX_ARR_SIZE 100

int * find_fibonacci_primes(int arr[]) {

    return 0;
}

short int is_prime(unsigned int value) {
    if (!(value & 1)) return 0;
    return 0;
}

int main(void) {
    // Initialise relavant variables
    int arrSize, arr[MAX_ARR_SIZE];

    // Take array input
    printf("Enter input array size: ");
    scanf("%d", &arrSize);
    printf("Enter values: ");
    for (int i = 0; i < arrSize; i++) {
        scanf("%d", &arr[i]);
    }

    find_fibonacci_primes(arr);
    return 0;
}