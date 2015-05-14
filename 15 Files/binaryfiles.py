#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

def main():
    buffersize = 50000
    infile = open('olives.jpg', 'rb')
    outfile = open('new.jpg', 'wb')

    buffer = infile.read(buffersize)

    while len(buffer):
        outfile.write(buffer)
        print('50k', end='')
        buffer = infile.read(buffersize)

    print()
    print('Done')

if __name__ == "__main__": main()

# open('olives.jpg', 'rb').read(size)
# open('new.jpg', 'wb').write(open('olives.jpg', 'rb').read(size))