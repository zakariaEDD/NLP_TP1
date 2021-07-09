#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().system('pip install transformers')
get_ipython().system('pip install flair')
get_ipython().system('pip install torch')
get_ipython().system('pip install pytorch_pretrained_bert')
from transformers import AutoTokenizer
from flair.data import Sentence
from flair.models import SequenceTagger
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM


# ## Load DATA

# In[ ]:


text = 'ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و المقادير الهندسية و غيرها، أن تتعامل على أنها أجسام جبرية، و أعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان موجودا من قبل، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل'


# ## Tokenization

# In[15]:


PRE_TRAINED_MODEL_NAME = 'bert-base-cased'
tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)
tok = tokenizer.tokenize(text)
do_lower_case=False

print( text)
print(tok)


# In[ ]:




