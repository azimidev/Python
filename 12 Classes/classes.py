#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

class Duck:

    def __init__(self, value, value2):
        self._v = value
        self._v2 = value2


    def quack(self):
        print('Quaaack!', self._v, self._v2)

    def walk(self):
        print('Walks like a duck.',  self._v, self._v2)

def main():
    donald = Duck(53, 34)
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
