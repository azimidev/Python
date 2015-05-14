#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

import bitstring

def main():
    a = bitstring.BitString(bin = '01010101')
    print(a.hex, a.bin, a.unit)

if __name__ == "__main__": main()
