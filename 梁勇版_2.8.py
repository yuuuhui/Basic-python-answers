masswater = eval(input("Enter the amount of water in kg:"))
initialT = eval(input("Enter the initial temperature:"))
finalT = eval(input("Enter the final temperature:"))
Q = masswater * (finalT - initialT) * 4184
print("the energy required is {}".format(Q))
