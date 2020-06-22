# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:01:04 2020

@author: Tanu
"""
#TO WIN THE GAME THE TOTAL SCORE SHOULD BE EQUAL TO 20
import random
while(1):
    list=[1,2,3,4,5,6]
    a2=0
    b2=0
    c2=0
    d2=0
    while(1): 
        print("\n*************** PRAYER 1 ****************\n")
        input("THROW THE DICE TO PRESS(p):")
        a=random.choice(list)
        a1=a
        print("OUTCOME 1:",a1)
        a2=a2+a1
        print("TOTAL SCORE OF PRAYER 1 IS:",a2)
        if a2>=20:
            print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 1 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
            break
        if a1==6:
            input("AGAIN THROW THE DICE TO PRESS(p):")
            a=random.choice(list)
            a1=a
            a2=a2+a1
            print("OUTCOME 2:",a)
            print("TOTAL SCORE OF PRAYER 1 IS:",a2)
            if a2>=20:
                print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 1 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                break
            if a1==6:
                input("AGAIN THROW THE DICE TO PRESS(p):")
                a=random.choice(list)
                a1=a
                print("OUTCOME 3:",a)
                if a1==6:
                    a2=a2+a1-6-6-6
                    print("TOTAL SCORE OF PRAYER 1 IS:",a2)
                    if a2>=20:
                        print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 1 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                        break
                else:
                    a2=a2+a1
                    print("TOTAL SCORE OF PRAYER 1 IS:",a2)
                    if a2>=20:
                        print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 1 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                        break
    
        print("\n*************** PRAYER 2 ****************\n")
        input("THROW THE DICE TO PRESS(p):")
        b=random.choice(list)
        b1=b
        print("OUTCOME 1:",b1)
        b2=b2+b1
        print("TOTAL SCORE OF PRAYER 2 IS:",b2)
        if b2>=20:
            print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 2 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
            break
        if b1==6:
            input("AGAIN THROW THE DICE TO PRESS(p):")
            b=random.choice(list)
            b1=b
            b2=b2+b1
            print("OUTCOME 2:",b)
            print("TOTAL SCORE OF PRAYER 2 IS:",b2)
            if b2>=20:
                print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 2 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                break
            if b1==6:
                input("AGAIN THROW THE DICE TO PRESS(p):")
                b=random.choice(list)
                b1=b
                print("OUTCOME 3:",b)
                if b1==6:
                    b2=b2+b1-6-6-6
                    print("TOTAL SCORE OF PRAYER 2 IS:",b2)
                    if b2>=20:
                        print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 2 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                        break
                else:
                    b2=b2+b1
                    print("TOTAL SCORE OF PRAYER 2 IS:",b2)
                    if b2>=20:
                        print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 2 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                        break
    
        print("\n*************** PRAYER 3 ****************\n")
        input("THROW THE DICE TO PRESS(p):")
        c=random.choice(list)
        c1=c
        print("OUTCOME 1:",c1)
        c2=c2+c1
        print("TOTAL SCORE OF PRAYER 3 IS:",c2)
        if c2>=20:
            print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 3 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
            break

        if c1==6:
            input("AGAIN THROW THE DICE TO PRESS(p):")
            c=random.choice(list)
            c1=c
            c2=c2+c1
            print("OUTCOME 2:",c)
            print("TOTAL SCORE OF PRAYER 3 IS:",c2)
            if c2>=20:
                print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 3 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                break

            if c1==6:
                input("AGAIN THROW THE DICE TO PRESS(p):")
                c=random.choice(list)
                c1=c
                print("OUTCOME 3:",c)
                if c1==6:
                    c2=c2+c1-6-6-6
                    print("TOTAL SCORE OF PRAYER 3 IS:",c2)
                    if c2>=20:
                        print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 3 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                        break

                else:
                    c2=c2+c1
                    print("TOTAL SCORE OF PRAYER 3 IS:",c2)
                    if c2>=20:
                        print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 3 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                        break

        print("\n*************** PRAYER 4 ****************\n")
        input("THROW THE DICE TO PRESS(p):")
        d=random.choice(list)
        d1=d
        print("OUTCOME 1:",d1)
        d2=d2+d1
        print("TOTAL SCORE OF PRAYER 4 IS:",d2)
        if d2>=20:
            print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 4 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
            break
        if d1==6:
            input("AGAIN THROW THE DICE TO PRESS(p):")
            d=random.choice(list)
            d1=d
            d2=d2+d1
            print("OUTCOME 2:",d)
            print("TOTAL SCORE OF PRAYER 4 IS:",d2)
            if d2>=20:
                print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 4 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                break
            if d1==6:
                input("AGAIN THROW THE DICE TO PRESS(p):")
                d=random.choice(list)
                d1=d
                print("OUTCOME 3:",d)
                if d1==6:
                    d2=d2+d1-6-6-6
                    print("TOTAL SCORE OF PRAYER 4 IS:",d2)
                    if d2>=20:
                        print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 4 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                        break
                else:
                    d2=d2+d1
                    print("TOTAL SCORE OF PRAYER 4 IS:",d2)
                    if d2>=20:
                        print("\n@@@@@@@@@@@@@@@@@@@@ PRAYER 4 IS WIN @@@@@@@@@@@@@@@@@@@@\n")
                        break
    
        p=input("To continue the game press (y) otherwise press (n):")
        if p=="n":
            break
    q=input("for exit press y:")
    if q=="y":
        break




