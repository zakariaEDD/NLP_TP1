#!/usr/bin/env python
# coding: utf-8

# # NLP  
# TP1 NLTK ENGLISH

# # load DATA

# In[58]:


PH="""ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا. و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل"""


# # Tokenization 

# In[59]:


import nltk
from nltk import word_tokenize
tok = nltk.word_tokenize(PH)

print(tok)


# # Stop words

# In[60]:


from nltk.corpus import stopwords
Mot = [w for w in tok if w not in stopwords.words('arabic')]
Mot


# # Part-of-Speech Tagging

# In[4]:


Pos1 = nltk.pos_tag(tok)
print(Pos1)
print('\n')


# # Stemming 

# In[45]:


from nltk.stem.porter import PorterStemmer

from nltk.stem import WordNetLemmatizer


# In[50]:


stm = PorterStemmer()

text_stem = [stm.stem(w) for w in Mot]

text_stem


# # Lemmatization

# In[49]:


lm = WordNetLemmatizer()

text_lem = [wnl.lemmatize(w) for w in Mot]
text_lem


# In[ ]:





# In[ ]:




