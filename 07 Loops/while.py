#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

def main():
    # simple fibonacci series
    # the sum of two elements defines the next set
    a, b = 0, 1
    while b < 50:
        print(b, end=' ')
        a, b = b, a + b

if __name__ == "__main__": main()
