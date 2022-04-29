from utils import *
pk = 4

try:
    load = load_students()[pk - 1]
except IndexError:
    load = 0



print(load)
