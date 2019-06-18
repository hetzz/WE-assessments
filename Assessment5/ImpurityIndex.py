def Letter_occurence_computation(sentence):
    letter_array = [0 for i in range(26)]
    for i in sentence.lower() :
        try :
            letter_array[ord(i) - 97] += 1
        except IndexError:
            pass
    return letter_array

def impurity_count(sentence):
    impurity_index = 0
    letter_array = Letter_occurence_computation(sentence)
    vowels = ['a','e','i','o','u']
    impurity_increment = [0, 0.5, 0.7 ,1, 3]
    for i in range(len(letter_array)):
        if(chr(i + 97) in vowels ):
            if(letter_array[i] == 2) :
                impurity_index += impurity_increment[1]
        if(chr(i + 97) not in vowels and  letter_array[i] == 2) :
            impurity_index += impurity_increment[2]
        if(letter_array[i] == 3):
            impurity_index += impurity_increment[3] 
        if(letter_array[i] > 3):
            impurity_index += impurity_increment[4] 
    return (impurity_index)

sentence = "Old brother fox jumps over the lazy dog."
print(impurity_count(sentence))
