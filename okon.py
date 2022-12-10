#!/usr/bin/python3
fname= input("Please enter a text file: ")

name = []
#opening file
with open(fname, 'r') as f:
    fr = f.readlines()
    mike = open('okon'+fname,'w')
    for uname in fr:
        #replacing apostrophe
        name = uname[:-1]
        name = uname.replace("'", '')
        #replacin hyphen
        user = name.replace("-", '')
        #replacing empty spaces
        username = user.replace(" ", '')
        #indicing part to string to create abreviation
        username = username[0:1] + username[2:4].upper()
        mike.writelines(username + ' ')
        print(username)