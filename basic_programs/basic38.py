#How to reverse a string in Python
def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # It will return the reverse string to the caller function  
     
str = "JavaTpoint"    # Given String       
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) # Function call  


#  Reverse a string    
# using  slice syntax   
# reverse(str) Function to reverse a string   
def reverse(str):   
    str = str[::-1]   
    return str   
    
s = "JavaTpoint"  
print ("The original string  is : ",s)   
print ("The reversed string using extended slice operator  is : ",reverse(s)) 