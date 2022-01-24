# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

def swapList(newList):
    size = len(newList)
     
    # Swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
newList = [5, 10, 15, 20, 25]
 
print(swapList(newList))
