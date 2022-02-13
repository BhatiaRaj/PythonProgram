# Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates. 
Num1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Ans = []

cal = len(Num1)

for d in range(cal):
     if Num1[d] in Num2 and Num1[d] not in Ans:
         Ans.append(Num1[d])
print(Ans)