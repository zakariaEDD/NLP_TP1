#!/usr/bin/env python
# coding: utf-8

# # NLP_Tp1_Spacy_Arabic
# 
# ## load data

# In[23]:


import spacy
from spacy.lang.ar import *

nlp = Arabic()
txt=nlp("""ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا. و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل""")


# # Tokenazition and pos tagging
# 

# In[19]:


for tok in txt:
    print(tok.text)
    print(tok.pos_)
    print( tok.tag_)
    


# # Lemmatization
# 

# In[20]:


for word in txt:
    print(word.text + ':' , word.lemma_ )    


# In[26]:


#sentence tokenization
for s in txt.sents:
    print(s)


# In[31]:


import spacy
from spacy.lang.en import *

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()

# Create the pipeline 'sentencizer' component
#sbd = nlp.create_pipe('sentencizer')

# Add the component to the pipeline
nlp.add_pipe(sbd)

text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""

#  "nlp" Object is used to create documents with linguistic annotations.
doc = nlp(text)

# create list of sentence tokens
sents_list = []
for sent in doc.sents:
    sents_list.append(sent.text)
print(sents_list)


# In[ ]:




