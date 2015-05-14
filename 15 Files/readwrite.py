#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

def main():
    f = open('lines.txt')
    for line in f.readlines():
        print(line, end = '')

if __name__ == "__main__": main()
