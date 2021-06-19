#!/usr/bin/env python
# coding: utf-8

# ## importing dependencies 
# 
# 

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense,LSTM,Dropout


# ### importing the training data of GOOG historical prices

# In[2]:


data = pd.read_csv('trainData.csv') 


# In[3]:


data.info()


# ## choosing the close column 
# 

# In[4]:


data["Close"]=pd.to_numeric(data.Close,errors='coerce') #turning the Close column to numeric
data = data.dropna() #romeving the NA values
data


# In[5]:


data.iloc[:,4:5]


# In[6]:


trainData = data.iloc[:,4:5].values #selecting only the closing prices for training
trainData


# ## scaling the values in the range of 0-1 for best preformances 

# In[7]:


sc = MinMaxScaler(feature_range=(0,1))
trainData = sc.fit_transform(trainData)
trainData.shape


# ## preparing the data for LSTM
#  since its a time series problem we took 60 as timestep for our learning : given *60 closing values* as an input data the *61st value* is our output

# In[8]:


X_train = []
y_train = []

for i in range (60,1149): #60 : timestep // 1149 : length of the data
    X_train.append(trainData[i-60:i,0]) 
    y_train.append(trainData[i,0])

X_train,y_train = np.array(X_train),np.array(y_train)


# In[9]:


X_train


# In[10]:


y_train


# ps : LSTM take a 3D tensor (seq_len,timestep,batch_size)

# In[11]:


X_train


# In[12]:


X_train = np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1)) #adding the batch_size axis
X_train.shape


# ## building the model 

# In[13]:


model = Sequential()

model.add(LSTM(units=100, return_sequences = True, input_shape =(X_train.shape[1],1)))
model.add(Dropout(0.2))

model.add(LSTM(units=100, return_sequences = True))
model.add(Dropout(0.2))

model.add(LSTM(units=100, return_sequences = True))
model.add(Dropout(0.2))

model.add(LSTM(units=100, return_sequences = False))
model.add(Dropout(0.2))

model.add(Dense(units =1))
model.compile(optimizer='adam',loss="mean_squared_error")


# In[14]:


hist = model.fit(X_train, y_train, epochs = 20, batch_size = 32, verbose=2)


# ### ploting the training loss
# 

# In[15]:


plt.plot(hist.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()


# ### testing the model on new data
# 

# In[16]:


print(len(inputClosing_scaled))
inputClosing_scaled


# In[17]:


testData = pd.read_csv('GOOG.csv') #importing the test data
testData["Close"]=pd.to_numeric(testData.Close,errors='coerce') #turning the close column to numerical type
testData = testData.dropna() #droping the NA values
testData = testData.iloc[:,4:5] #selecting the closing prices for testing
y_test = testData.iloc[60:,0:].values #selecting the labels 
y_test[0:10]


# In[18]:


#input array for the model
inputClosing = testData.iloc[:,0:].values 
inputClosing_scaled = sc.transform(inputClosing)
inputClosing_scaled[0:10]


# In[19]:


inputClosing_scaled.shape
X_test = []
length = len(testData)
testData


# In[20]:


length


# In[21]:


timestep


# In[22]:


timestep = 60
for i in range(timestep,length): #doing the same preivous preprocessing 
    X_test.append(inputClosing_scaled[i-timestep:i,0])
print(len(X_test))
X_test[0:3]


# In[23]:


X_test = np.array(X_test)
X_test


# In[24]:


X_test = np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
X_test


# In[25]:


y_pred = model.predict(X_test) #predicting the new values


# In[26]:


predicted_price = sc.inverse_transform(y_pred) #inversing the scaling transformation for ploting 


# ### ploting the results

# In[27]:


plt.plot(y_test, color = 'blue', label = 'Actual Stock Price')
plt.plot(predicted_price, color = 'red', label = 'Predicted Stock Price')
plt.title('GOOG stock price prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

