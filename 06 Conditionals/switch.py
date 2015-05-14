#!/usr/local/bin/python3.4
# switch.py by Amir Hassan Azimi [http://parsclick.net/]

def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )
    v = 'five'
    print(choices.get(v, 'other'))

if __name__ == "__main__": main()
