import argparse

parser = argparse.ArgumentParser(description="Code to add two numbers")
parser.add_argument('-lst', type=str, nargs='+', help="Second number to add")
args = parser.parse_args()
finalList = []
for entry in args.lst:
    try:
        finalList.append(int(entry))
    except:
        print('You have inserted a string. Please enter only integers')
        exit(1)
total=0
for num in finalList:
    total = total + num
print(str(int(total/len(finalList))))

