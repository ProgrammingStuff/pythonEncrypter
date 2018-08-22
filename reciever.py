from random import randint

def sendString(string):
        text_file = open("traffic.txt", "w")
        text_file.write(string)
        text_file.close()

def getString():
    text_file = open("traffic.txt", "r")
    return text_file.read()

def run(lo1, hi1):

    values = getString().split("\n")

    shared_key = values[0]

    mod = values[1]

    y = randint(lo1, hi1)

    encryptedKey = (int(shared_key)**y)%int(mod)

    print("y=" + str(y) + ", sending: " + str(encryptedKey))

    sendString(getString() + "\n" + str(encryptedKey))

    #-------------------------------------------------------

    key = (int(values[3])**y)%int(mod)
    print("reciever key = " + str(key))
