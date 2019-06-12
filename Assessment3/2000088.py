# def rle(input_string) :
#     reduced_list = []
#     count = 0
#     while( count < len(input_string) - 1):
#         letter_count = 1 
#         while(input_string[count] == input_string[count+1]):
#             letter_count += 1
#             count += 1
#         if( letter_count > 2) :
#             reduced_list.append(str(letter_count))
#         elif( letter_count == 2):
#             reduced_list.extend(input_string[count])
#         else :
#             count += 1
#         reduced_list.append(input_string[count])


#     return "".join(reduced_list)

from itertools import groupby

def get_groups(s):
    print([group[1] for group in groupby(s)])
    return [list(group[1] )for group in groupby(s)]

def rle_block(b):
    size = len(b)
    if size <= 2 :
        return size * b[0]
    
    return str(size) + b[0]

def rle(s):
    return "".join([rle_block(block) for block in get_groups(s)])

print(rle("aaaaaabbbbaacgf"))
########################################################################

def irle(reduced_string):
    reduced_list = list(reduced_string)
    expanded_string = []

    for i in range(len(reduced_list)) :
        try:
            value = int(reduced_list[i])
            for x in range (value):
                expanded_string.append(reduced_list[i+1] )
        except ValueError:
            pass 
            
    return "".join(expanded_string)

print(rle("aaabbbthd"))
print(irle("3a2bc4c"))