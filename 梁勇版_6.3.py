
def reverse(number):
    return str(number)[::-1]



def isPalindrome(number):
    reverse(number)
    if reverse(number) == str(number):
        isPalindrome = True
        
    else:
        isPalindrome  = False
    print(isPalindrome)
isPalindrome(122)
