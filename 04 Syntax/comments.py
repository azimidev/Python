#!/usr/local/bin/python3.4

#Main method
def main():
    for n in primes():
        if n > 100: break
        print(n)


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

#Generator
def primes(n = 1):
   while(True):
       if isprime(n): yield n #Generator keyword
       n += 1

if __name__ == "__main__": main()
