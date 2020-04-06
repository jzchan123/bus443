import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Code to add two numbers")
    parser.add_argument('--lst', type=str, nargs='+', help="Second number to add")
    args = parser.parse_args()
    #print(args.lst)
    combineList = []
    combineString = ""
for word in args.lst:
    for character in word:            
        if character not in combineList:
            combineList.append(character)
            combineString = combineString + character
    combineString = combineString + " "

print(combineString)




#7combinelist makes new list
#8 makes a new empty string
#9 for every word in args.lst.....
#10 adds a space for every word
#11 for each individual chracter inside word
#12
#13 if that individual chracter is not inside combine list
#14 adds the chracter into the list
#15 adds the individual list characters into the string
#17 prints the string
