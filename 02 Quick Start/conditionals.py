#!/usr/local/bin/python3.4

a,b = 0,1

if a < b:
 print('a ({}) is less than b ({})'.format(a, b))
else:
 print('a ({}) is not less than b ({})'.format(a, b))

print("baroon" if a < b else "barf")