#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

class Duck:
    def quack(self): print('Quaaack!')
    def walk(self): print('Walks like a duck.')
    def bark(self): print('The duck cannot bark')
    def fur(self): print('The duck has feathers')

class Dog:
    def bark(self): print('woof!')
    def fur(self): print('the dog has brown and white fur')
    def walk(self): print('Walks like a dog.')
    def quack(self): print('the dog cannot quaaack!')

def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald) #run
    in_the_pond(fido) #run

def in_the_forest(cat):
    cat.bark()
    cat.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

    # Python's objects don't care what the name of the class is!
#    for o in (donald, fido):
#        o.quack()
#        o.walk()
#        o.bark()
#        o.fur()

if __name__ == "__main__": main()
