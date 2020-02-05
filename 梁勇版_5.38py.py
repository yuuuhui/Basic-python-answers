import time
timing = eval(input("Enter the number of seconds:"))









for i  in range(1,timing):
    print("{} seconds remaining".format(timing - 1 ))
    timing -= 1
    time.sleep(1)

print("Stopped")    
    







