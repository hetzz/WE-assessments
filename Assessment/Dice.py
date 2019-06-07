import random
def RandomThrow ():
    dice1, dice2 = random.randint(1,6), random.randint(1,6)
    return dice1, dice2

def frequencyTable () :
    freq_table = []
    for i in range(1000) :
        dice1, dice2 = RandomThrow()
        if (freq_table_keys.find([dice1,dice2]) != -1) :
            freq_table