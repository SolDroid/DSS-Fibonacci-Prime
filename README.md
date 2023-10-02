# Fibonacci Prime Finder
**Dalhousie Space Society
Software & OBC Competency Test**

Simple functions in both C and Python which take in an input of an array / list of integers and return an array / list of the integers which were both included in the Fibonacci Sequence and prime

## 1.0 Function Overview
The function `find_fibonacci_primes(arr)` is present in both [fibonacciPrime.py](https://github.com/SolDroid/DSS-Fibonacci-Prime/blob/main/fibonacciPrime.py) and [fibonacciPrime.c](https://github.com/SolDroid/DSS-Fibonacci-Prime/blob/main/fibonacciPrime.c). This function is the primary objective of both of these scripts, both of them contain other functionality purely for testing. The way in which this function decides whether or not a given value is both prime and within the Fibonacci sequence happens in 5 total steps.

## 2.0 Step Overview
The five iterated steps of the `find_fibonacci_primes(arr)` function are as follows:
1. Check for basic cases [(2.1)](#21-basic-cases-if-value--3)
2. Find the index of the number within the Fibonacci sequence [(2.2)](#22-find-fibonacci-sequence-index-fibonacci_indexvalue)
3. Check if the index exists [(2.2)](#22-find-fibonacci-sequence-index-fibonacci_indexvalue)
4. Check if the index is prime [(2.3)](#23-check-if-the-index-is-prime-is_primefibindex)
5. Finally, check if the value is prime [(2.4)](#24-check-primality-is_primevalue)

All of these steps are iterated over for each `value` within the input array `arr`, resulting in a total big oh of **O(1)** at the absolute ideal, **~O($n$)** at worst, and ~**O($\sqrt{n}$)** for most non-prime Fibonacci numbers (why these are not exact big oh values is explained in [2.3](#23-check-if-the-index-is-prime-is_primefibindex)). Given that **O(1)** occurs when the values are not within the Fibonacci sequence, this can be taken to be the typical big oh. If any of these steps fail to find that `value` is prime or within the Fibonacci sequence then the current iteration is ended with `continue`.

### 2.1 Basic Cases: `if (value <= 3)`
The trivial basic cases of the function are when `value` is 3 or less, 1 being non-prime, 2 and 3 being prime and in the Fibonacci sequence. Checking for these cases immediately prevents unecessary operations at the cost of very little performance while ensuring that all values too small to abide by later approximations are filtered out.

### 2.2 Find Fibonacci Sequence Index: `fibonacci_index(value)`
This operation is the most mathematically complex in order to acheive a big oh of **O(1)** itself. Instead of iterating over all Fibonacci numbers until `value`, this operation takes advantage of Binet's Formula [(Source)](https://r-knott.surrey.ac.uk/Fibonacci/fibFormula.html#section1):
$$ F_{ib}(n)=\frac{\phi^n-(-\phi^{-n})}{\sqrt{5}}, n\in\Z^+,\phi=\frac{\sqrt{5} + 1}{2}$$
Which produces an exact integer value for a number in the Fibonacci sequence at any integer index $n$, where $F_{ib}(0)=0$ and $F_{ib}(1)=1$. The issue with this formula is that no exact inverse can be found with standard algebraic operations. The solution to this is some simple function analysis, also courtesy of the same [source](https://r-knott.surrey.ac.uk/Fibonacci/fibFormula.html#section1). As the $-\phi^{-n}$ term tends to 0 for $n>0$, the only term in the numerator that is actually relevant for positive integer values of n is $\phi^n$. Using the approximation that only includes this term we can derive an approximate inverse as follows:
$$F_{ib}(n)=F\approx\frac{\phi^n}{\sqrt{5}}\to n\approx\frac{\ln(\sqrt{5}F)}{\ln(\phi)}$$
This being my own math. If a rounded value of $n$ is then put back into $F_{ib}(n)$, the nearest element of the Fibonacci sequence can be found. However, if $F_{ib}(n)$ doesn't match `value` exactly then `value` must hence not be an element of the Fibonacci sequence. This function then returns either the index within the Fibonacci sequence or -1 if the number is not within the sequence. -1 is returned as it is assumed that `arr` will only contain unsigned integers.

### 2.3 Check if the Index is Prime: `is_prime(fibIndex)`
Aside from the use of the `is_prime` function in this step which will be elaborated upon in the next step, the rationale for why a prime index is checked for first is important for optimization. As all prime numbers within the Fibonacci sequence have a prime index, (aside from $F_{ib}(4)=3$, which is filtered out by the basic case checks in [2.1](#21-basic-cases-if-value--3)) checking if the index is prime before checking if the value itself is prime allows for major optimisation in most situations ([Fibonacci prime index source](https://proofwiki.org/wiki/Fibonacci_Prime_has_Prime_Index_except_for_3)). As the index of a number within the Fibonacci sequence is always smaller than the value, the big oh of this operation alone is less than **O($\sqrt{n}$)** (This big oh being described in [2.4](#24-check-primality-is_primevalue)). Taking our formula for the Fibonacci index of a number from section [2.2](#22-find-fibonacci-sequence-index-fibonacci_indexvalue), we can say that the big oh is
$$O(\sqrt{\frac{\ln(\sqrt{5}n)}{\ln(\phi)}})$$
or more accurately for big oh notation, simply **O($\sqrt{ln(n)}$)**.

### 2.4 Check Primality: `is_prime(value)`
The `is_prime` function used within both scripts is quite simple, the only real optimisation is that it iterates over all factors only up to the square root of `value` as any factors less than this will multiply with a corresponding value greater than `sqrt(value)`, meaning all iteration past `sqrt(value)` is redundant. If an element of `arr` passes this final check, then it is considered to be a prime Fibonacci number and is added to the output array.

## 3.0 Table of Big Oh Notation
|Worst Case|Second Worst|Best Case|Typical|
|:---------|:----------:|:-----:|--------:|
|**O($\sqrt{n\ln(n)}$)**|**O($\sqrt{\ln(n)}$)**|**O(1)**|**O(1)**|
|$n$ is a Fibonacci prime|$n$ is a Fibonacci number|$n$ is not a Fibonacci number|Most values of $n$|
|Ends at [2.4](#24-check-primality-is_primevalue)|Ends at [2.3](#23-check-if-the-index-is-prime-is_primefibindex)|Ends at [2.1](#21-basic-cases-if-value--3) or [2.2](#22-find-fibonacci-sequence-index-fibonacci_indexvalue)|Ends at [2.1](#21-basic-cases-if-value--3) or [2.2](#22-find-fibonacci-sequence-index-fibonacci_indexvalue)|