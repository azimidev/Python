#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

def main():
    try:
        for line in readfile('lines.oc'): print(line.strip()) # strip() is same as end=''
    except IOError as e:
        print('could not open the file: ', e)
    except ValueError as e:
        print('bad file name ', e)

def readfile (filename):
    if filename.endswith(suffix)
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Wrong file extension!')

if __name__ == "__main__": main()
