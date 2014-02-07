
# #Exercise: Using Dictionaries

# ##Dictionary
# 
# Consider the following dictionarys:

# In[1]:

zipcodes = {}
zipcodes['80403'] = 'Boulder, CO, Boulder County'
zipcodes['80123'] = 'Monument, CO El Paso County'
zipcodes['80919'] = 'Colorado Springs, CO El Paso County'


# In[2]:

names = {}
names['Pat'] = '80403'
names['Bob'] = '80919'
names['Jane'] = '80132'


# It's efficient because I can linke a `name` with `zipcode` information.  Then I can print `name` information.

# In[3]:

name = 'Pat'

print name, 'lives in', zipcodes[names[name]]


# Out[3]:

#     Pat lives in Boulder, CO, Boulder County
# 

# 1. Add a phone number to the `names` dictionary. 
# 
#     Your new output should look like:
# 
#         Pat is from Boulder CO, Boulder County :  xxx-xxx-xxxx
