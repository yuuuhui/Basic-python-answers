numstudent = int(input("Enter the number of students:"))
list = []
num = 0
while num < numstudent:
    score=eval(input("Enter the score of a student:"))
    list.append(score)
    num += 1
else:
    print("the max score is {}".format(max(list)))
    print("the minimum score is {}".format(min(list)))

