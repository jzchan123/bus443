

import argparse

if __name__ == '__main__':
 parser = argparse.ArgumentParser(description="Code to add two numbers")
 parser.add_argument('-lst', action ='append' , type=int, nargs='+', help="Second number to add")
 args = parser.parse_args()
 
 masterList = []

 for x in args.lst:
     newList = []
     for y in x:
         newList.append(str(y*y))
     masterList.append(newList)

print(masterList)
         

