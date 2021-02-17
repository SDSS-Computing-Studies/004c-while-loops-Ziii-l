#!python3

import time

counter = 0
while True:
    print(" xx ", end ="", flush=True)
    time.sleep(0.25)
    counter = counter + 1
    print(counter, end="", flush=True)
    if counter > 50:
        break