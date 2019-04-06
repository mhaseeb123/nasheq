#=============================================================================
# Group Number:         18
# PROGRAMMER1:          Muhammad Haseeb
# PANTHER ID1:          6166473
#
# PROGRAMMER2:          Rafay Khan
# PANTHER ID2:          2346111
#
# CLASS:                CAP5507
# SECTION:              U01
# SEMESTER:             Spring 2019
# CLASSTIME:            M/W 6:25-7:40 pm
#
# Project:              Game Theory Coding Assignment
# DUE:                  04/07/2019
#
# CERTIFICATION:        I certify that this work is my own and that
#                       none of it is the work of any other person.
#=============================================================================

#!/usr/bin/env python
# coding: utf-8

# # Import Packages

import numpy as np
import scipy as sp
import pandas as pd
import random

# # User Input

# User strategy sets
s1 = ["A1","A2","A3","A4","A5","A6","A7","A8","A9"]
s2 = ["B1","B2","B3","B4","B5","B6","B7","B8","B9"]

# Max size of strategy set 
szmax = 9

# Initialize rows and columns to 1
rows = 0
cols = 0
mode = "I"

print ("---------------------------------------")
print (" CAP5507: Game Theory Coding Assignment")
print ("     Muhammad Haseeb, Rafay Khan")
print ("---------------------------------------\n")

while (mode != "R" and mode != "M"):
    mode = input("Enter (R)andom or (M)anual payoffs entries: ")

while (rows < 1 or rows > szmax):
    rows = input("Enter the number of rows: ")
    rows = int (rows)

while (cols < 1 or cols > szmax):
    cols = input("Enter the number of cols: ")
    cols = int(cols)


# # Instantiate and Initialize Data

p1 = np.ones((rows, cols), dtype=np.int32)
p2 = np.ones((rows, cols), dtype=np.int32)

# Initialize with Random Payoffs
if (mode == "R"):
    for x in range(rows):
        for y in range(cols):
            p1[x,y] = random.randint(-99,99)
            p2[x,y] = random.randint(-99,99)

    print ("------------------------------------")
    print ("Player: Player1's strategies")
    print ("------------------------------------")

    sp1 = "{"
    for kk in range(rows):
        sp1 += s1[kk] + ", "
    sp1 = sp1[:-2]
    sp1+= "}"
    print (sp1)

    print ("\n------------------------------------")
    print ("Player: Player1's payoffs")
    print ("------------------------------------")


    for kk in range(rows):
        sp1 = ""
        for ll in range (cols):
            if (p1[kk, ll] < 0):
                sp1 += str(p1[kk, ll]) + ",\t"
            else:
                sp1 += " " + str(p1[kk, ll]) + ",\t"
        sp1 = sp1[:-2]
        print (sp1)
    
    
    print ("\n------------------------------------")
    print ("Player: Player2's strategies")
    print ("------------------------------------")

    sp2 = "{"
    for kk in range(cols):
        sp2 += s2[kk] + ", "
    sp2 = sp2[:-2]
    sp2+= "}"
    print (sp2)
    
    print ("\n------------------------------------")
    print ("Player: Player2's payoffs")
    print ("------------------------------------")


    for kk in range(rows):
        sp2 = ""
        for ll in range (cols):
            if (p2[kk, ll] < 0):
                sp2 += str(p2[kk, ll]) + ",\t"
            else:
                sp2 += " " + str(p2[kk, ll]) + ",\t"
        sp2 = sp2[:-2]
        print (sp2)
    
    
# Manual payoffs from the user input
if (mode == "M"):
    print ("Manual Entries")
    # Input from user
    for x in range(rows):
        for y in range(cols):
            p1[x,y], p2[x,y] = map(int, input("Enter payoff for ( "+ s1[x] + ", " + s2[y] + " ) = ").split(','))
            if (p1[x,y] > 99):
                p1[x,y] = 99
            if (p1[x,y] < -99):
                p1[x,y] = -99
            if (p2[x,y] > 99):
                p2[x,y] = 99
            if (p2[x,y] < -99):
                p2[x,y] = -99
                
        print ("---------------------------")


# # Print Game Function (input: p1, p2)

def printgame(p1,p2):
    # Horizontal line
    hline = "   "
    hline += "-" * (14 * (cols) + 1)
    
    st2 = " " * 10
    
    for ll in range (cols):
        st2 += s2[ll] + " " * 12 # strategy name will take the rest of 2 characters making 15 chars gap

    print (st2[:-12])
    print (hline)
    
    for ii in range (rows):
        rstr = s1[ii] + " |"
        for jj in range (cols):
            kal = str(p1[ii,jj])
            kali = str(p2[ii,jj])
            rstr += "  (" + kal
            rstr += " " * (3-len(kal))
            rstr += "," + kali
            rstr += " " * (3-len(kali))
            rstr += ")  |"
        print (rstr)
        print (hline)
    
# Print the game
print ("\n=======================================")
print ("Display Normal Form")
print ("=======================================")

printgame(p1,p2)


# # Find Pure Nash Equilibrium in the game

# Initialize the Nash Equilibrium to false
nash = False

def nasheq(p1,p2, li1, li2):
    # Horizontal line
    hline = "   "
    hline += "-" * (14 * (cols) + 1)
    
    st2 = " " * 10
    
    for ll in range (cols):
        st2 += s2[ll] + " " * 12 # strategy name will take the rest of 2 characters making 15 chars gap

    print (st2[:-12])
    print (hline)
    
    for ii in range (rows):
        rstr = s1[ii] + " |"
        for jj in range (cols):
            kal = ""
            kali = ""
            if ((ii * cols + jj) in li1) == True:
                kal = "H"
            else:
                kal = str(p1[ii,jj])
                
            if ((ii * cols + jj) in li2) == True:
                kali = "H"
            else:
                kali = str(p2[ii,jj])
            rstr += "  ("
            rstr += " " * (3-len(kal)) + kal
            rstr += "," + kali
            rstr += " " * (3-len(kali))
            rstr += ")  |"
        print (rstr)
        print (hline)

# Nash Eq sites
l1 = []
l2 = []
mx = 0

# Compute Max payoff locations for player 1
for i in range(cols):
    mx = -10000000
    for j in range(rows):
        if (p1[j,i] >= mx):
            mx = p1[j,i]
            ii = i
            jj = j
    #print (mx, ii, jj)
    l1.append([jj * cols + ii])

print ("\n")
    
# Compute Max payoff locations for player 2
for i in range(rows):
    mx = -10000000
    for j in range(cols):
        if (p2[i,j] >= mx):
            mx = p2[i,j]
            ii = i
            jj = j
    #print (mx, ii, jj)
    l2.append([ii * cols + jj])

li1 = np.array(l1)
li1 = np.reshape(li1, (1,np.product(li1.shape)))[0]
li2 = np.array(l2)
li2 = np.reshape(li2, (1,np.product(li2.shape)))[0]

neq = np.intersect1d(li1, li2)

print ("=======================================")
print ("Nash Pure Equilibrium Locations")
print ("=======================================")

nasheq(p1,p2, li1, li2)

if (neq.size > 0):
    nash = True
    prnt_str = "\nPure Nash Equilibrium(s): "
    for l in range (neq.size):
        prnt_str += "(" + s1[int(neq[l]/cols)] + "," + s2[int(neq[l] % cols)] + ")" + "  "
    print (prnt_str)
else:
    print ("\nNash Equilibrium(s): None")



# # Belief Matrices

# Belief arrays
theta1 = np.zeros(rows, dtype=float)
theta2 = np.zeros(cols)
Theta1 = "("
Theta2 = "("

# Summation of probabilities
pr = 0

if (rows != 2 or cols != 2):
    # Create random belief about player 1
    for k in range(theta1.size):
        theta1[k] = random.randint(0,99)
        pr += theta1[k]

    for k in range(theta1.size):
        theta1[k] /= pr

    # Reset the summation
    pr = 0

    # Create random beliefs about player 2
    for k in range(theta2.size):
        theta2[k] = random.randint(0,99)
        pr += theta2[k]

    for k in range(theta2.size):
        theta2[k] /= pr

    # Print the matrix
    for k in range (theta1.size):
        Theta1 += str(theta1[k].round(2)) + ", "
        
    for k in range (theta2.size):
        Theta2 += str(theta2[k].round(2)) + ", "
    
    Theta1 = Theta1[:-2]
    Theta2 = Theta2[:-2]
    Theta1 += ")"
    Theta2 += ")"
    
#    print(Theta1)
#    print(Theta2)


# # Best Response

# Payoffs
u1s = np.zeros(rows, dtype=float)
u2s = np.zeros(cols, dtype=float)

if (rows != 2 or cols != 2):
    # Compute payoffs
    for i in range(rows):
        for j in range(cols):
            u1s[i] += theta2[j] * p1[i,j]

    # Compute payoffs
    for i in range(cols):
        for j in range(rows):
            u2s[i] += theta1[j] * p2[j,i]

    print ("\n----------------------------------------------")
    print ("Player 1 Expected Payoffs with Player 2 Mixing")
    print ("----------------------------------------------")
    for rr in range (u1s.size):
        print ("U1("+ s1[rr]+ ", ", Theta2, ") = ", u1s[rr])
    
    print ("\n----------------------------------------------")
    print ("Player 1 Best Response with Player 2 Mixing")
    print ("----------------------------------------------")
    print ("BR1", Theta2, "= {"+ s1[u1s.argmax()]+"}\n")
    
    print ("----------------------------------------------")
    print ("Player 2 Expected Payoffs with Player 1 Mixing")
    print ("----------------------------------------------")
    for rr in range (u2s.size):
        print ("U2("+ s2[rr]+ ", ", Theta1, ") = ", u2s[rr])

    # Print Best Response
    print ("\n----------------------------------------------")
    print ("Player 2 Best Response with Player 1 Mixing")
    print ("----------------------------------------------")
    print ("BR2",Theta1," = {" + s2[u2s.argmax()]+"}")


# # Expected Payoffs

# Expected payoff for player 1
exp1 = 0
# Expected payoff for player 2
exp2 = 0

if (rows != 2 or cols !=2):
    # Compute
    for i in range(rows):
        exp1 += u1s[i] * theta1[i]

    # Compute
    for i in range(cols):
        exp2 += u2s[i] * theta2[i]
    
    # Print
    print("\n------------------------------------------------------")
    print("Player 1 & 2 Expected Payoffs with both Players Mixing")
    print("------------------------------------------------------")
    print ("U1(", Theta1, ", ", Theta2,") = ", exp1)
    print ("U1(", Theta2, ", ", Theta1,") = ", exp2)


# # Case: 2x2 Game

# # Indifference 2 x 2 Game

# Indifference Probabilities
p = 0
q = 0

if (rows == 2 and cols == 2 and nash == False):
    coeff = p1[0,0] - p1[0,1] - p1[1,0] + p1[1,1]
    const = p1[1,1] - p1[0,1]
    q = const/coeff

    coeff = p2[0,0] - p2[1,0] - p2[0,1] + p2[1,1]
    const = p2[1,1] - p2[1,0]
    p = const/coeff

    print ("\n------------------------------------------")
    print ("Player 1 & 2 Indifferent Mix Probabilities")
    print ("------------------------------------------")
    # Print Indifference Probabilities
    print ("Player 1 probability of strategies ("+ s1[0] + ") =", p)
    print ("Player 1 probability of strategies ("+ s1[1] +") =", 1-p)
    print ("Player 2 probability of strategies ("+ s2[0] +") =", q)
    print ("Player 2 probability of strategies ("+ s2[1] +") =", 1-q)

elif (rows == 2 and cols == 2 and nash == True):
    print ("\nNormal Form has Pure Strategy Equilibrium")


# In[114]:


ex = input ("\nPress Enter to Exit.. ")
