n = 8

a = 1




for i in range(1,9):
    print("  " * (n - i ),end = " ")

    while a < 2 ** (i):
        a *= 2
        c = a
        b = a
        k = 1
        while c > 1:
            print(k, end = " ")
            c /= 2
            k *= 2
                  
            
            
        
        while b > 2:
            b /= 2
            print(int(b/2 ),end = " ")
            
            
    print("\n")







"""
a = 1
while a < 129:
    print(a)
    a *= 2
"""  
