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
# :caption: Basic Industries
# 
# stocks/fbprophet/BHP.ipynb
# stocks/fbprophet/LIN.ipynb
# stocks/fbprophet/RIO.ipynb
# stocks/fbprophet/VALE.ipynb
# stocks/fbprophet/SHW.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Capital Goods
# 
# stocks/fbprophet/TSLA.ipynb
# stocks/fbprophet/TM.ipynb
# stocks/fbprophet/TMO.ipynb
# stocks/fbprophet/HON.ipynb
# stocks/fbprophet/BA.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Consumer Durables
# 
# stocks/fbprophet/CSAN.ipynb
# stocks/fbprophet/GE.ipynb
# stocks/fbprophet/ABB.ipynb
# stocks/fbprophet/AME.ipynb
# stocks/fbprophet/FERG.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Consumer Non-Durables
# 
# stocks/fbprophet/PG.ipynb
# stocks/fbprophet/KO.ipynb
# stocks/fbprophet/NKE.ipynb
# stocks/fbprophet/PEP.ipynb
# stocks/fbprophet/UL.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Consumer Services
# 
# stocks/fbprophet/AMZN.ipynb
# stocks/fbprophet/BABA.ipynb
# stocks/fbprophet/WMT.ipynb
# stocks/fbprophet/HD.ipynb
# stocks/fbprophet/DIS.ipynb
# stocks/fbprophet/CMCSA.ipynb
# stocks/fbprophet/NFLX.ipynb
# stocks/fbprophet/T.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Energy
# 
# stocks/fbprophet/XOM.ipynb
# stocks/fbprophet/CVX.ipynb
# stocks/fbprophet/BBL.ipynb
# stocks/fbprophet/TOT.ipynb
# stocks/fbprophet/BP.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Finance
# 
# stocks/fbprophet/JPM.ipynb
# stocks/fbprophet/BAC.ipynb
# stocks/fbprophet/WFC.ipynb
# stocks/fbprophet/MS.ipynb
# stocks/fbprophet/C.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Health Care
# 
# stocks/fbprophet/JNJ.ipynb
# stocks/fbprophet/UNH.ipynb
# stocks/fbprophet/PFE.ipynb
# stocks/fbprophet/ABT.ipynb
# stocks/fbprophet/ABBV.ipynb
# stocks/fbprophet/NVS.ipynb
# stocks/fbprophet/MRK.ipynb
# stocks/fbprophet/LLY.ipynb
# stocks/fbprophet/DHR.ipynb
# stocks/fbprophet/NVO.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Miscellaneous
# 
# stocks/fbprophet/V.ipynb
# stocks/fbprophet/MA.ipynb
# stocks/fbprophet/PYPL.ipynb
# stocks/fbprophet/EDU.ipynb
# stocks/fbprophet/PDD.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Public Utilities
# 
# stocks/fbprophet/TMUS.ipynb
# stocks/fbprophet/NEE.ipynb
# stocks/fbprophet/DUK.ipynb
# stocks/fbprophet/SO.ipynb
# stocks/fbprophet/D.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Technology
# 
# stocks/fbprophet/AAPL.ipynb
# stocks/fbprophet/MSFT.ipynb
# stocks/fbprophet/GOOG.ipynb
# stocks/fbprophet/GOOGL.ipynb
# stocks/fbprophet/FB.ipynb
# stocks/fbprophet/TSM.ipynb
# stocks/fbprophet/NVDA.ipynb
# stocks/fbprophet/ASML.ipynb
# stocks/fbprophet/ADBE.ipynb
# stocks/fbprophet/INTC.ipynb
# stocks/fbprophet/ORCL.ipynb
# stocks/fbprophet/CSCO.ipynb
# stocks/fbprophet/CRM.ipynb
# stocks/fbprophet/AVGO.ipynb
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Transportation
# 
# stocks/fbprophet/UPS.ipynb
# stocks/fbprophet/UNP.ipynb
# stocks/fbprophet/BKNG.ipynb
# stocks/fbprophet/FDX.ipynb
# stocks/fbprophet/CSX.ipynb
# ```
# 
