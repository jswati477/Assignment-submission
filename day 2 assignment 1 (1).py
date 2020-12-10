#!/usr/bin/env python
# coding: utf-8

# Assignment No.1
# 

# Q.1.Try 5 Different functions of the String in Python.
# For example - index, split function.

# 1. count() -

# In[2]:


txt = "I love Mangoes, Mangoes are my favorite fruit, I ate Mangoes "

x = txt.count("Mangoes")

print(x)


# 2. format() -

# In[3]:


txt = "For only {price:.3f} dollars!"
print(txt.format(price = 100))


# 3. capitalize() -

# In[4]:


txt = "hello, and welcome to my Home."

x = txt.capitalize()

print (x)


# 4. isalpha() -

# In[5]:


txt = "IndustryX"

x = txt.isalpha()

print(x)


# 5.splitlines() -

# In[6]:


txt = "Thank you for the dinner\nWelcome to the party"

x = txt.splitlines()

print(x)


# Q.2.Try 5 Different functions of the List object in Python.

# 1. extend() -

# In[7]:


fruits = ['Grapes', 'kiwi', 'Mango']

cars = ['Honda', 'Ford', 'Hundai']

fruits.extend(cars)

print(fruits)


# 2.pop() -

# In[8]:


fruits = ['apple', 'banana', 'cherry']

fruits.pop(2)

print(fruits)


# 3.remove()-

# In[9]:


flowers = ['Lili', 'Mogara', 'Rose']

flowers.remove("Lili")

print(flowers)


# 4.reverse() -

# In[10]:


fruits = ['Grapes', 'Mango', 'kiwi']

fruits.reverse()

print(fruits)


# 5.insert() -

# In[11]:


flowers = ['Champa', 'Mogara', 'lili']

flowers.insert(2, "Rose")

print(flowers)


# Q.3.Experiment with at least 5 default functions of Dictionary.
# 

# 1.fromkeys() -

# In[12]:


a = ('key1', 'key2', 'key3')
b = 10

thisdict = dict.fromkeys(a, b)


print(thisdict)


# 2.popitem() -

# In[13]:


car = {
  "brand": "Hyudai",
  "model": "Grand i10",
  "year": 1965
}

car.popitem()

print(car)


# 3.update()-

# In[14]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


# 4.get()-

# In[15]:


car = {
  "brand": "Hyndai",
  "model": "Grand i10",
  "year": 1965
}

x = car.get("model")

print(x)


# 5. values()-

# In[16]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)


# In[ ]:




