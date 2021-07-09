#!/usr/bin/env python
# coding: utf-8

# # NLP_Tp1_Spacy_En
# 
# ## load data
# 

# In[ ]:


get_ipython().system('pip install -U spacy')
get_ipython().system('python -m spacy download en_core_web_sm')
import spacy
from spacy import displacy 
nlp = spacy.load('en_core_web_sm')
text = nlp("""Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely
the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from
the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational
numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new
development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the
subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a
way which had not happened before.""")


# # Tokenization et pos tagging

# In[29]:




for t in text:
    print(t.text,":",t.pos_, ":",t.tag_)


#  # Lemmatization

# In[31]:



for word in text:
    print(word.text,  ":" , word.lemma_ )


#  # Stemming

# In[33]:



p_stemmer = PorterStemmer()
for words in text :
   print(words.text + '---------' + p_stemmer.stem(words.text))
   
   


# # chunking
# 

# In[22]:


for chunk in text.noun_chunks:
    print(chunk.text,chunk.label_,chunk.root.text)
    


# In[23]:


for token in text:
    print("{0}/{1} <-- {2} <-- {3}/{4}".format(
    token.text, token.tag_, token.dep_, token.head.text, token.head.tag_) )  
    


# # parsing 
# 

# In[24]:


#parsing visualistation
displacy.render(text, style='dep', jupyter = True, options={'distance' : 100})


# In[35]:


entities=[(i, i.label_, i.label) for i in text.ents]
entities


# In[ ]:




