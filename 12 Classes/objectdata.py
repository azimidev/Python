#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

class Duck:

    def __init__(self, **kwargs):
        self.variables = kwargs

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)

def main():
    donald = Duck(feet = 2, amir = 4)
    donald.set_variable('color', 'blue')
    print(donald.get_variable('feet'))
    print(donald.get_variable('color'))
    print(donald.get_variable('amir'))

if __name__ == "__main__": main()
