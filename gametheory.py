
# coding: utf-8

# # Import Packages

# In[39]:


import numpy as np
import scipy as sp
import pandas as pd
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


# # User Input

# In[40]:


# User strategy sets
s1 = ["A1","A2","A3","A4","A5","A6","A7","A8","A9"]
s2 = ["B1","B2","B3","B4","B5","B6","B7","B8","B9"]

# Max size of strategy set 
szmax = 9

# Initialize rows and columns to 1
rows = 0
cols = 0
mode = "I"

while (mode != "R" and mode != "M"):
    mode = input("Enter (R)andom or (M)anual payoffs entries\n")

while (rows < 1 or rows > szmax):
    rows = input("Enter the number of rows: ")
    rows = int (rows)

while (cols < 1 or cols > szmax):
    cols = input("Enter the number of rows: ")
    cols = int(cols)


# # Instantiate and Initialize Data

# In[43]:


p1 = np.ones((rows, cols), dtype=np.int32)
p2 = np.ones((rows, cols), dtype=np.int32)

# Initialize with Random Payoffs
if (mode == "R"):
    for x in range(rows):
        for y in range(cols):
            p1[x,y] = random.randint(-99,99)
            p2[x,y] = random.randint(-99,99)

print (p1)
print (p2)

# Manual payoffs from the user input
if (mode == "M"):
    # Input from user
    p1
    p2


# # Print Game Function (input: p1, p2)

# In[42]:


#def printgame(p1,p2):


# # Find Pure Nash Equilibrium in the game

# In[51]:


nash = False


# # Belief Matrices

# In[44]:


# Belief arrays
theta1 = np.zeros(rows, dtype=float)
theta2 = np.zeros(cols)

# Summation of probabilities
pr = 0

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
print(theta1)
print(theta2)


# # Best Response

# In[45]:


# Payoffs
u1s = np.zeros(rows, dtype=float)
u2s = np.zeros(cols, dtype=float)

for i in range(rows):
    for j in range(cols):
        u1s[i] += theta2[j] * p1[i,j]

for i in range(cols):
    for j in range(rows):
        u2s[i] += theta1[j] * p2[j,i]

print (u1s)
print (u2s)
print (u1s.argmax())
print (u2s.argmax())


# # Expected Payoffs

# In[46]:


# Expected payoff for player 1
exp1 = 0
# Expected payoff for player 2
exp2 = 0

# Compute
for i in range(rows):
    exp1 += u1s[i] * theta1[i]

# Compute
for i in range(cols):
    exp2 += u2s[i] * theta2[i]
    
# Print
print (exp1)
print (exp2)


# # Indifference 2 x 2 Game

# In[55]:


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

    # Print Indifference Probabilities
    print (p)
    print (1-p)
    print (q)
    print (1-q)

elif (nash == True):
    print ("Nash Equilibrium Exists")

