num = int(input("Enter the number of students:"))
count = 0
scorelist = []
while count < num:
    score = eval(input("Enter the score of a student:"))
    scorelist.append(score)
    print(scorelist)
    
    count += 1
else:
    print("The highest is score is",max(scorelist))
    scorelist.remove(max(scorelist))
    print("the second highest is",max(scorelist))
