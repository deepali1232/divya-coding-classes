#How to convert int to string in Python
n = 25  
# check  and print type of num variable  
print(type(n))  
print(n)  
  
# convert the num into string  
con_num = str(n)  
  
# check  and print type converted_num variable  
print(type(con_num))  
print(con_num)  



n = 10  
  
# check and print type of n variable  
print(type(n))  
  
# convert the num into a string and print  
con_n = "% s" % n  
print(type(con_n))  



n = 10  
  
# check  and print type of num variable  
print(type(n))  
  
# convert the num into string and print  
con_n = "{}".format(n)  
print(type(con_n))  



n = 10  
  
# check  and print type of num variable  
print(type(n))  
  
# convert the num into string  
conv_n = f'{n}'  
  
# print type of converted_num  
print(type(conv_n))   