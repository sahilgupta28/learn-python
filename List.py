#List

numbers = [1,1.3,33]

print(numbers) #List start from 0 index and it will print whole list

print(numbers[1]) #It will print only one element which @ index 1

print(numbers[1]+1) #It will add one in a copy of list index 1 but real list will be unchages

print(numbers) # No effect of add operator on real list.

numbers.append(10) #add new valve @ the end of list
print(numbers)

numbers.pop() # remove last element of list.
print(numbers)