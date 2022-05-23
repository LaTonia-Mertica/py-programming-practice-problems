numsList = [44, 7, 13]

numsList.sort()

first = 0
last = len(numsList) - 1
mid = (first + last) // 2
val = int(input("Enter Searchable Number Value: "))

found = False

while (first <= last and not found):
    mid = (first + last) // 2
    if numsList[mid] == val:
        print(f'Found at Location {mid}')
        found = True
    else:
        if val < numsList[mid]:
            last = mid - 1
        else:
            first = mid + 1
if found == False:
    print('Number Not Found!') 
