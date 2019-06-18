def isPangram(sentence):
    letter_array = [0 for i in range(26)]
    for i in sentence.lower() :
        try :
            letter_array[ord(i) - 97] = 1
        except IndexError:
            pass
    print(letter_array)
    
    return letter_array.count(0) == 0

def Panagram(sentence) :
    return isPangram(sentence)

sentence = input()
print("The fact that the input string is a panagram is : ",Panagram(sentence))
