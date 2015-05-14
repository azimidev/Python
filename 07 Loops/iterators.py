#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

def main():
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end='')

if __name__ == "__main__": main()
