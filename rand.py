import time

def rand_val(x):

    random=int(time.time()*1000)

    random %= x

    return random

x=int(input())

print(rand_val(x))
