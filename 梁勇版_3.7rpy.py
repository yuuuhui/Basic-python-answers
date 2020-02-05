'''
lowercase 97 - 122, uppercase 65 - 90
'''
import time
t = time.time()
print(t)

a = int(t) % 26 + 65   #lowercase            
b = int(t) % 26 + 97  #uppercase
print(a,b)

print(chr(a),chr(b))
