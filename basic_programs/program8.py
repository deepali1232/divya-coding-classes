str1="this is my first string"
print(str1)
str2='this is my second string'
print(str2)
str3='''this
string 
has 
lot of 
lines'''
print(str3)

    #extract starting chars from string
name = "Divya Srivastava"
print(name[0],name[1],name[2],name[3],name[4],name[5])

#last chars from string
print(name[-1],name[-2],name[-3],name[-4],name[-5],name[-6],name[-7],name[-8],name[-9],name[-10])
print(name[0:6])

#reverse a string
print(name[::-1])

#find len of string
print(len(name))

#ocnvert in lower case
print(name.lower())

#convert in upper case
print(name.upper())

#replace a substring
print(name)
print(name.replace('ya','bu'))
print(name.replace('a','s'))

#number of occurence of substring
name1="my name is divya .my home name is heena."
print(name1.count('my'))
print(name1.count('d'))

#find the index of substring
s1 = 'aishwarya is mad girl'
print(s1.find('g'))

#split string
s2="my fav fruit is apple,mango,banana,pear."
print(s2.split(','))
s3 = 'my name is divya.'
print(s3.split('e'))