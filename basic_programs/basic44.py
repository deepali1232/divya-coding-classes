#Python Program to generate a Random String
# create a program to generate the random string of given letters.  
import random  
import string  
def specific_string(length):  
    sample_string = 'pqrstuvwxy' # define the specific string  
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    print(" Randomly generated string is: ", result)  
  
specific_string(8) # define the length  
specific_string(10)  



# create a program to generate a string with or without repeating the characters.  
import random  
import string  
print("Use of random.choice() method")  
def specific_string(length):  
     
    letters = string.ascii_lowercase # define the lower case string  
     # define the condition for random.choice() method  
    result = ''.join((random.choice(letters)) for x in range(length))  
    print(" Random generated string with repetition: ", result)  
  
specific_string(8) # define the length  
specific_string(10)  
  
  
print("") # print the space  
print("Use of random.sample() method")  
def WithoutRepeat(length):  
    letters = string.ascii_lowercase # define the specific string  
    # define the condition for random.sample() method  
    result1 = ''.join((random.sample(letters, length)))   
    print(" Random generated string without repetition: ", result1)  
  
WithoutRepeat(8) # define the length  
WithoutRepeat(10)   



import random  
import string  
def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  
  
# define the length of the letter is eight and digits is four  
print("Generated random string of first string is:", random_string(8, 4))  
  
# define the length of the letter is seven and digits is five  
print("Generated random string of second string is:", random_string(7, 5))  




import random   
import string  
import secrets # import package  
num = 10 # define the length of the string  
# define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
  
# print the Secure string   
print("Secure random string is :"+ str(res))  