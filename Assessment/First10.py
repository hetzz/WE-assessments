import math

def iscalculateExpression(a, b,c):
    a = math.pow(a,3)
    b = math.pow(b,3)
    c = math.pow(c,2)
    return a + b == c

#############################################################

def generateTriples(num_of_literals):
    triples = []
    a = 0
    b = 0
    c = 0
    while (len(triples) != num_of_literals) :
        if (iscalculateExpression(a,b,c)) :
            tripl = [a ,b, c]
            triples.append(tripl)
        else :
            a += 1
            b += 1

#######################################################
num_of_literals = int(input())