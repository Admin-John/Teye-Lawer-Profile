#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols


# In[12]:


import pandas as pd


# In[66]:


Anova_data = pd.read_clipboard('clipboard')


# In[67]:


Anova_data.head(3)


# In[68]:


import statsmodels.api as sm
from statsmodels.formula.api import ols


# ### Perform two-way ANOVA

# In[69]:


model = ols('Hours ~ C(TEACHER) + C(WORK) + C(TEACHER):C(WORK)', data=Anova_data).fit()
sm.stats.anova_lm(model, typ=2)


# In[70]:


print(model.summary())


# ### Post-Hoc Test

# In[71]:


from statsmodels.stats.multicomp import pairwise_tukeyhsd


# In[76]:


import numpy as np


# In[94]:


tukey=pairwise_tukeyhsd(endog=Anova_data['WORK'], groups=Anova_data['TEACHER'],alpha=0.05)


# In[95]:


print(tukey)


# #### Data Used is here

# In[60]:


print(Anova_data)


# In[62]:


Anova_data.info(all)


# In[ ]:




