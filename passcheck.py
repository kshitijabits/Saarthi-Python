import re

password = input("Enter password:")

flag=1

if len(password)<6 or len(password)>16:
    print("\nInvalid length, min length 6 characters max 16.")
else:
    regex = re.compile('[@_!"#$%^&\'*+,-.()<=@>?/\|}{~:;^_`]') 
    if(regex.search(password) == None):
        #print("\nNo special characters, password invalid.")
        flag=0
        
    regex1 = re.compile('[a-z]') 
    if(regex1.search(password) == None):
        #print("\nNo a-z characters, password invalid.")
        flag=0
        
    regex2 = re.compile('[A-Z]') 
    if(regex.search(password) == None):
        #print("\nNo A-Z characters, password invalid.")
        flag=0
        
    regex3 = re.compile('[0-9]') 
    if(regex3.search(password) == None):
        #print("\nNo digits 0-9 characters, password invalid.")
        flag=0
       
    if flag==1:
        print("\nValid password created successfully.")
    else:
        print("\nPassword is missing some character from a-z A-Z 0-9 or any special character")

