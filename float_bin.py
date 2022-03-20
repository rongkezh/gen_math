#!/usr/bin/env python
# coding: utf-8

# In[1]:


def float_bin(number, places = 3):
  
    # split() separates whole number and decimal 
    # part and stores it in two separate variables
    whole, dec = str(number).split(".")
  
    # Convert both whole number and decimal  
    # part from string type to integer type
    whole = int(whole)
    dec = int (dec)
  
    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(whole).lstrip("0b") + "."
  
    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):
  
        # Multiply the decimal value by 2 
        # and separate the whole number part
        # and decimal part
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
  
        # Convert the decimal part
        # to integer again
        dec = int(dec)
  
        # Keep adding the integer parts 
        # receive to the result variable
        res += whole
  
    return res
  
# Function converts the value passed as
# parameter to it's decimal representation
def decimal_converter(num): 
    while num > 1:
        num /= 10
    return num


# In[10]:


float_bin(0.9,4)


# In[ ]:




