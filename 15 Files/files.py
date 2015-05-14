#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

def main():
    buffersize = 100000
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w')
    buffer = infile.read(buffersize)

    while len(buffer):
        outfile.write(buffer)
        print('100k', end=' ')
        buffer = infile.read(buffersize)

    print()
    print('Done!')

if __name__ == "__main__": main()
