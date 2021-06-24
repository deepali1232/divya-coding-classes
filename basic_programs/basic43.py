#How to concatenate two strings in Python
# Defining strings  
str1 = "Hello "  
str2 = "Devansh"  
  
# + Operator is used to strings concatenation  
str3 = str1 + str2  
print(str3)   # Printing the new combined string  



str1 = "Hello"  
str2 = "JavaTpoint"  
  
# join() method is used to combine the strings  
print("".join([str1, str2]))  
  
# join() method is used to combine  
# the string with a separator Space(" ")  
str3 = " ".join([str1, str2])  
  
print(str3)  


str1 = "Hello"  
str2 = "JavaTpoint"  
  
# % Operator is used here to combine the string  
print("% s % s" % (str1, str2)) 


 
str1 = "Hello"  
str2 = "JavaTpoint"  
  
# format function is used here to   
# concatenate the string   
print("{} {}".format(str1, str2))   
  
# store the result in another variable   
str3 = "{} {}".format(str1, str2)   
  
print(str3)