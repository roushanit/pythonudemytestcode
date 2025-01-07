from threading import *
from time import *

class alphabets(Thread):
    def run(self):
        for i in range(65,91):            
            print(chr(i))
            sleep(1)

t = alphabets()
t.start()
for i in range(65,91):
    print(i)
    sleep(1)

t.join()    
