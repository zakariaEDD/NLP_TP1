#!/usr/bin/env python
# coding: utf-8

# # NLP  
# TP1 NLTK ENGLISH

# # Tokenization 

# In[27]:


import nltk
from nltk import word_tokenize
PH = """Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely
the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from
the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational
numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new
development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the
subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a
way which had not happened before."""
tok = nltk.word_tokenize(PH)

print(tok)


# # Stop words

# In[28]:


from nltk.corpus import stopwords
Mot = [w for w in tok if w not in stopwords.words('english')]
Mot


# # Part-of-Speech Tagging

# In[29]:


Pos1 = nltk.pos_tag(tok)
print(Pos1)
print('\n')


# # Stemming 

# In[32]:


from nltk.stem.porter import PorterStemmer

from nltk.stem import WordNetLemmatizer


# In[40]:


stm = PorterStemmer()

text_stem = [stm.stem(w) for w in words_sw]

text_stemmer


# # Lemmatization

# In[41]:


lm = WordNetLemmatizer()

text_lem = [wnl.lemmatize(w) for w in words_sw]
text_lem


# In[ ]:





# In[ ]:




