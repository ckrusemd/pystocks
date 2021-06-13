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


# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: FB Prophet
# 
# stocks/fbprophet/AAPL.ipynb
# stocks/fbprophet/MSFT.ipynb
# stocks/fbprophet/AMZN.ipynb
# stocks/fbprophet/GOOG.ipynb
# stocks/fbprophet/GOOGL.ipynb
# stocks/fbprophet/FB.ipynb
# stocks/fbprophet/TSM.ipynb
# stocks/fbprophet/TSLA.ipynb
# stocks/fbprophet/BABA.ipynb
# stocks/fbprophet/JPM.ipynb
# stocks/fbprophet/V.ipynb
# stocks/fbprophet/JNJ.ipynb
# stocks/fbprophet/NVDA.ipynb
# stocks/fbprophet/WMT.ipynb
# stocks/fbprophet/UNH.ipynb
# stocks/fbprophet/BAC.ipynb
# stocks/fbprophet/MA.ipynb
# stocks/fbprophet/HD.ipynb
# stocks/fbprophet/PG.ipynb
# stocks/fbprophet/DIS.ipynb
# stocks/fbprophet/PYPL.ipynb
# stocks/fbprophet/ASML.ipynb
# stocks/fbprophet/CMCSA.ipynb
# stocks/fbprophet/XOM.ipynb
# stocks/fbprophet/ADBE.ipynb
# stocks/fbprophet/KO.ipynb
# stocks/fbprophet/TM.ipynb
# stocks/fbprophet/INTC.ipynb
# stocks/fbprophet/ORCL.ipynb
# stocks/fbprophet/CSCO.ipynb
# stocks/fbprophet/NFLX.ipynb
# stocks/fbprophet/CRM.ipynb
# stocks/fbprophet/PFE.ipynb
# stocks/fbprophet/NKE.ipynb
# stocks/fbprophet/T.ipynb
# stocks/fbprophet/ABT.ipynb
# stocks/fbprophet/PEP.ipynb
# stocks/fbprophet/CVX.ipynb
# stocks/fbprophet/ABBV.ipynb
# stocks/fbprophet/NVS.ipynb
# stocks/fbprophet/WFC.ipynb
# stocks/fbprophet/AVGO.ipynb
# stocks/fbprophet/MRK.ipynb
# stocks/fbprophet/LLY.ipynb
# stocks/fbprophet/BHP.ipynb
# stocks/fbprophet/UPS.ipynb
# stocks/fbprophet/TMO.ipynb
# stocks/fbprophet/DHR.ipynb
# stocks/fbprophet/NVO.ipynb
# ```
# 
