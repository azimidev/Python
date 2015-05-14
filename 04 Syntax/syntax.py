#!/usr/local/bin/python3.4

class Nedah:

    def __init__(self, kind = "girl"):
        self.kind = kind

    def whatKind(self):
        return self.kind

#------------------------------------------------

def main():
    girl = Nedah()
    niceGirl = Nedah("nice")

    print(girl.whatKind())
    print(niceGirl.whatKind())

if __name__ == "__main__": main()