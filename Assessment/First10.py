import math

def iscalculateExpression(a, b, c):
    a = math.pow(a,3)
    b = math.pow(b,3)
    c = math.pow(c,2) 
    return a + b == c

#############################################################

def generateTriples(num_of_literals):
    triples = []
    a = 1
    b = 2
    c = 3
    while (len(triples) < num_of_literals) :
        if (iscalculateExpression(a,b,c)) :
            tripl = [a ,b, c]
            triples.append(tripl)
        
        a += 1
        b += 1
        c += 1
    
    return triples

#######################################################
num_of_literals = int(input())
print(generateTriples(num_of_literals))