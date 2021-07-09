#!/usr/bin/env python
# coding: utf-8

# # NLP_Tp1_huggingface_En

# In[19]:


get_ipython().system('pip install transformers')
get_ipython().system('pip install flair')
from transformers import AutoTokenizer

from flair.data import Sentence
from flair.models import SequenceTagger


# ## Load DATA

# In[20]:


text="Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational numbers,irrational numbers, geometrical magnitudes, etc., to all be treated as \"algebraic objects\". It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itselfin a way which had not happened before."


# # Tokenization
# 

# In[16]:


token=AutoTokenizer.from_pretrained("bert-base-uncased")
tok=token.tokenize(text)
print(tok)


# # pos tagging

# In[28]:


from flair.data import Sentence
from flair.models import SequenceTagger
tagger = SequenceTagger.load("flair/pos-english")
sentence = Sentence(text)
tagger.predict(sentence)

for w in sentence.get_spans('pos'):
    print(w)
    
    


# In[ ]:





# In[ ]:




