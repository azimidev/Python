#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

import time, saytime

t = time.localtime()
print("Content-type: text/html\n")
print(
    "In London, United Kingdom, it is now " +
    saytime.saytime_t(t).words() +
    time.strftime(', on %A, %d %B %Y.')
)


