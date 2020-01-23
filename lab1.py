# new string where first and last char are exchanged
# Program to check if substring is in the string
# Count the number of vowels using a set
# Determine how many times string occurs using set
# Determine how many times string occurs recursively
# Factorial

"""
#String exchange
a=list(input("Enter a string "))
print(a)
x=a[-1]
a[-1]=a[0]
a[0]=x
a=''.join(a)
print("Swapped string is "+a)
"""



"""
#String search
a=input("Enter first string").lower()
b=input("Enter second String").lower()
a
if (a.find(b)==-1):
    print("Not found")
else:
    print("Found")
"""


"""
#Vowel counter
vowel = set("aeiouAEIOU")
a=input("Enter string to be checked")
count=0
for al in a:
    if al in vowel:
        count=count+1
print("No of vowels ",count)
"""        

"""
#Substring pattern counter
a=input("Enter string")
b=input("String to be searched")
print(type(b))
print(len(b))
res= 0
sub_len = len(b) 
for i in range(len(a)):
    if  b in a[i:i+sub_len]: 
        res += 1
print(res)
"""

def countSubstring(str1, str2): 
    n1 = len(str1)
    n2 = len(str2)     
    if (n1 == 0 or n1 < n2): 
        return 0
  
    # Recursive Case 
    # Checking if the first 
    # substring matches 
    if (str1[0 : n2] == str2): 
        return countSubstring(str1[n2 - 1:],  
                             str2) + 1 
  
    # Otherwise, return the count  
    # from the remaining index 
    return countSubstring(str1[n2 - 1:], str2) 


a=input("Enter first string")
b=input("Second string")
print(countSubstring(a,b))


'''
Factorial recursive
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return int(n*factorial(n-1))

n=int(input("Enter a number whose factorial is to be known"))
print(factorial(n))
'''

