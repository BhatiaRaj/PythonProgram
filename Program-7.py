# Write one line of Python that takes list a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] and makes a new list that has only the even elements of this list in it.

ML = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newlst = [i for i in ML if i % 2 == 0]
print(newlst)
