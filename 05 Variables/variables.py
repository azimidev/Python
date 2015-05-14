#!/usr/local/bin/python3.4



def main():
    d = dict(one=1, two=2, three=3, four=4, five='five')
    d['seven'] = 'haft'
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == "__main__": main()

