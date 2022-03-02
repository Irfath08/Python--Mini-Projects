#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import random

#Creating a combination of characters
char = list(string.ascii_letters + string.digits + "!@#$%^&*()")

            
def generate_random_passwords():
    ## length of password from the user
    length = int(input("Enter password length: "))

    ## shuffling the characters
    random.shuffle(char)
    
    password=[]
    for i in range(length):
        password.append(random.choice(char))
            
    #Shuffling the resultant password
    random.shuffle(password)
            
    #Converting the password from list to string and printing        
    print("".join(password))
    
#invoke the function            
generate_random_passwords()
            
    
            


# In[ ]:




