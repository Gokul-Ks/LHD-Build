#!/usr/bin/env python
# coding: utf-8

# In[1]:


alphabets="abcdefghijklmnopqrstuvwxyz"
message=input("Enter the message to encrypt: ")
encrypt,decrypt="",""
key=5

for letter in message:
    new_position=(alphabets.find(letter)+key)%len(alphabets)
    encrypt+=alphabets[new_position]


print("Encrypted message:",encrypt)


# In[2]:


encrypt


# In[3]:


encrypt2,decrypt2 = "","";

word1 = encrypt[int(len(encrypt)/2):]
word2 = encrypt[:int(len(encrypt)/2)]
encrypt2 = word1+word2


# In[4]:


encrypt2


# In[ ]:





# In[5]:


decrypt2


# In[6]:


key2 = 4
encrypt3, decrypt3 = "",""
for letter in encrypt2:
    new_position=(alphabets.find(letter)+key2)%len(alphabets)
    encrypt3+=alphabets[new_position]


# In[7]:


encrypt3


# In[8]:


for letter in encrypt3:
    new_position=(alphabets.find(letter)-key2)%len(alphabets)
    decrypt3+=alphabets[new_position]


# In[9]:


decrypt3


# In[10]:


word1 = decrypt3[:int(len(encrypt)/2)]
word2 = decrypt3[int(len(encrypt)/2):]
decrypt2 = word2+word1


# In[11]:


decrypt2


# In[12]:


for letter in decrypt2:
    new_position=(alphabets.find(letter)-key)%len(alphabets)
    decrypt+=alphabets[new_position]


# In[13]:


decrypt


# In[ ]:




