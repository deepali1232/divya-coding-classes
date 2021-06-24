#How to convert Bytes to string in Python
string1 = 'Welcome to JavaTpoint'  
print(type(string1))  
string2 = b'Welcome to JavaTpoint'  
print(type(string2))  


byteData = b"Lets eat a \xf0\x9f\x8d\x95!"  
# Let's check the type  
print(type(byteData))  
str1 = byteData.decode('UTF-8')  
print(type(str1))  
print(str1)  


import codecs  
byteData = b'Lets eat a \xf0\x9f\x8d\x95!'  
codecs.decode(byteData, 'UTF-8')  


byteData = b'Lets eat a \xf0\x9f\x8d\x95!'  
b1 = str(byteData, 'UTF-8')  
print(b1)  




str(b1, 'UTF-16') 