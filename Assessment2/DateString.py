def isAmbiguos(firstParam, seconParam):
    return (firstParam <= 12 and seconParam <= 12)


def dateAmbiguity(dateStr) :
    firstParam,seconParam,thirdParam = dateStr.split('/')
    return isAmbiguos(int(firstParam), int(seconParam))

date = input()
print("The fact that the date is ambiguous is ", dateAmbiguity(date))