#!/usr/local/bin/python3.4

# simple fibonacci series
# the sum of two elements defines the next set
a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
print("Done.")

