# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:50:22 2020

@author: Tanu
"""


while(1):
    print("Enter your choice for Prayer 1:(r/p/s)");
    p1=input("enter choice:");
    print("Enter your choice for Prayer 2:(r/p/s)");
    p2=input("enter choice:");  
    if p1=='r':
        if p2=='r':
            print("withdrawl")
        elif p2=='p':
            print("p2 win")
        elif p2=='s':
            print("p1 win")
        else:
            print("INVALID CHOICE OF PLAYER 2")
    if p1=='p':
        if p2=='r':
            print("p1 win")
        elif p2=='p':
            print("withdrawl")
        elif p2=='s':
            print("p2 win")
        else:
            print("INVALID CHOICE OF PLAYER 2")
    if p1=='s':
        if p2=='r':
            print("p2 win")
        elif p2=='p':
            print("p1 win")
        elif p2=='s':
            print("withdrawal")
        else:
            print("INVALID CHOICE OF PLAYER 2")
    if(p1!='r' and p1!='p' and p1!='s'):
        print("INVALID CHOICE OF PLAYER 1")
    p=input("***Do you want to exit the program***\nif yes then press 'y' otherwise 'n': ")
    if p=='y':
        break
        