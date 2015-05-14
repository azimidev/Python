#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

class Animal:

    def talk(self): print('Hey! I talk')
    def walk(self): print('Hey! I walk')
    def clothes(self): print('Hey I have nice clothes')

class Duck(Animal): #run

    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()
        print('Walks like a duck.')

class Dog(Animal):
    def clothes(self): print('I have a brown and white fur')

def main():
    donald = Duck()
    donald.quack()
    donald.walk() #overrides
    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.clothes()


if __name__ == "__main__": main()

