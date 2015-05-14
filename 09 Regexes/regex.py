#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '####'))

if __name__ == "__main__": main()
