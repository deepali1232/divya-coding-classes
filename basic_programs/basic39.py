#How to convert list to string in Python
# List is converting into string  
def convertList(list1):  
    str = ''  # initializing the empty string  
  
    return (str.join()) # return string  
  
list1 = ["Hello"," My", " Name is ","Devansh"] #passing string  
print(convertList(list1)) # Printin the converted string value  


# Converting list into string using list comprehension  
list1 = ["Peter", 18, "John", 20, "Dhanuska",26]  
  
convertList = ' '.join(map(str,list1)) # using map funtion  
  
print(convertList)  

# List is converting into string  
def convertList(list1):  
    str = ''  # initializing the empty string  
  
    for i in list1: #Iterating and adding the list element to the str variable  
        str += i  
  
    return str  
  
list1 = ["Hello"," My", " Name is ","Devansh"] #passing string   
print(convertList(list1)) # Printin the converted string value  