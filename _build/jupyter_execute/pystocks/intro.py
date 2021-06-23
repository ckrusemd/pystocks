#!/usr/bin/env python
# coding: utf-8

# # PyStocks
# 
# Stock Price Analytics of Yahoo! Finance data.
# 
# 
# Using the [Facebook Prophet](https://facebook.github.io/prophet/) framework right now. Will be looking into [Greykite](https://github.com/linkedin/greykite) as well.
# 
# You should be able to see the book at:
# 
# ```
# https://ckrusemd.github.io/pystocks/
# ```

# In[1]:


from datetime import datetime
import pytz
tz = pytz.timezone('Europe/Copenhagen')
print("Report extracted on " + datetime.now(tz).strftime("%d/%m/%Y %H:%M:%S") + ".")


# In[2]:


import IPython
print( IPython.sys_info() )

