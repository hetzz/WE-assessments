def addLiteralsToString(weave_str, str1, str2, str1_iter, str2_iter):
    weave_str += str1[str1_iter] + str2[str2_iter]
    str1_iter += 1
    str2_iter += 1
    return weave_str , str1_iter , str2_iter

####################################################################
def Str1LengthExceeds(weave_str, str1, str2, str1_iter, str2_iter, str2_len) :
    str1_iter = 0

    while(str2_iter < str2_len):
        weave_str , str1_iter , str2_iter = addLiteralsToString(weave_str, str1, str2, str1_iter, str2_iter)
    return weave_str , str1_iter , str2_iter

####################################################################
def Str2LengthExceeds(weave_str, str1, str2, str1_iter, str2_iter, str1_len) :
    str2_iter = 0

    while(str1_iter < str1_len):
        weave_str , str1_iter , str2_iter = addLiteralsToString(weave_str, str1, str2, str1_iter, str2_iter)
    return weave_str , str1_iter , str2_iter

########################################################################

def alternateStrings(str1,str2):

    weave_str = ""
    str1_len = len(str1)
    str2_len = len(str2)
    str1_iter = 0
    str2_iter = 0

    while(str1_iter < str1_len and str2_iter < str2_len):
        weave_str , str1_iter , str2_iter = addLiteralsToString(weave_str, str1, str2, str1_iter, str2_iter)

    if(str1_iter >= str1_len):
        weave_str , str1_iter , str2_iter = Str1LengthExceeds(weave_str, str1, str2, str1_iter, str2_iter, str2_len)
    
    elif (str2_iter >= str2_len):
        weave_str , str1_iter , str2_iter = Str1LengthExceeds(weave_str, str1, str2, str1_iter, str2_iter, str1_len)

    return weave_str

def usingZip(str1,str2) :
    weaved_string = zip(list(str1), list(str2))
    weave_str = ""
    for l in weaved_string :
        weave_str += "".join(l)
    if(len(str1) >  len(str2)):
        weave_str += str1[len(str1) - len(str2) :]
    elif(len(str2) >  len(str1)):
        weave_str += str2[len(str2) - len(str1) :]
    
    return weave_str



str1, str2 = input().split()
print(usingZip(str1, str2))
