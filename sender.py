from random import randint
import time
import reciever
import math
import random

def exp(base, exp):
    base = int(base)
    exp = int(exp)
    """ Fast power calculation using repeated squaring """
    if exp < 0:
        return 1 / power(base, -exp)
    ans = 1
    while exp:
        if exp & 1:
            ans *= base
        exp >>= 1
        base *= base
    return ans

def sendString(string):
    text_file = open("traffic.txt", "w")
    text_file.write(string)
    text_file.close()

def getString():
    text_file = open("traffic.txt", "r")
    return text_file.read()

startTime = time.time()

bits = 8

shared_key = 2
sendString(str(shared_key))

mod = 28684351666795074136653606360300759820312541610302799835942361343698472019524025437876718189599560527671826149891089779605333273978793039535700216098005372621114243383332462130588003615706177907482663737967899273995504154986949925222759421649504758817369155825193152532443560483993974172015781481548774943949855292984406047723983562736742870345005887222952635758798756158851888334297214092457568598109451177259993950280839582594393612428677023475078206698715034664877736530680899126794596936430152731825877089728377232078783231926312896550428155677769927532292781905842072873048543157900253911592406581088633629772989

sendString(getString() + "\n" + str(mod))

x = random.getrandbits(bits)

encryptedKey = exp(shared_key, x)%mod

print("x=" + str(x)+ ", sending: " + str(encryptedKey))

sendString(getString() + "\n\n" + str(encryptedKey))

#----------------------------------------------------------

reciever.run(bits)

values = getString().split("\n")

key = int(exp(str(values[4]), x))%int(mod)
bits = math.floor(math.log(key)/math.log(2)) + 1
print("sender key = " + str(key) + ", length in bit: " + str(bits))

endTime = time.time()
timeSpent = endTime - startTime
print("Time spent: " + str(timeSpent))
