from random import randint
import time
import reciever
import math

def sendString(string):
    text_file = open("traffic.txt", "w")
    text_file.write(string)
    text_file.close()

def getString():
    text_file = open("traffic.txt", "r")
    return text_file.read()

startTime = time.time()

hi = 5000000000000000000000000000000000000000
lo = 1000000000000000000000000000000000000000

hi1 = 100000
lo1 = 10000

shared_key = randint(lo, hi)
sendString(str(shared_key))

mod = randint(lo, hi)
sendString(getString() + "\n" + str(mod))

x = randint(lo1, hi1)

encryptedKey = (shared_key**x)%mod

print("x=" + str(x)+ ", sending: " + str(encryptedKey))

sendString(getString() + "\n\n" + str(encryptedKey))

#----------------------------------------------------------

reciever.run(lo1, hi1)

values = getString().split("\n")

key = (int(values[4])**x)%int(mod)
bits = math.floor(math.log(key)/math.log(2)) + 1
print("sender key = " + str(key) + ", length in bit: " + str(bits))

endTime = time.time()
timeSpent = endTime - startTime
print("Time spent: " + str(timeSpent))




