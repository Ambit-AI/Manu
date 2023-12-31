# -*- coding: utf-8 -*-
"""Sentiment_Analysis_using_BERT (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qe0p1hCziyn-5GBvDMFqDmXM2eDJI0LT
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install -q transformers

from transformers import pipeline
import pandas as pd
import numpy as np

df = pd.read_excel('/content/drive/MyDrive/Tower_Sentiment.xlsx', 'TOWER REAL')
# Dropping columns that do not need to be read
df.drop(df.columns[[4, 5, 8, 9]], axis=1, inplace=True)

# Truncate the DataFrame to contain only the first 3007 rows
df = df.iloc[:3007]

#Current amount of rows in dataset
print(len(df))

#dropping rows after 1500 because thats where we annotated to
#df.drop(df.index[1500:], inplace=True)

#Dropping all NaN data points
df_filled = df.dropna()

#Reset the "index" of the dataset
df_filled = df_filled.reset_index(drop = True)

#df_filled = df.fillna(" ")
old_word = 'Neural'
new_word = 'Neutral'

# Find rows containing the target word and replace it with the new word
df_filled['Sentiment'] = df_filled['Sentiment'].replace(old_word, new_word)

old_word = 'Positve'
new_word = 'Positive'
# Find rows containing the target word and replace it with the new word
df_filled['Sentiment'] = df_filled['Sentiment'].replace(old_word, new_word)

old_word = 'positive'
new_word = 'Positive'
# Find rows containing the target word and replace it with the new word
df_filled['Sentiment'] = df_filled['Sentiment'].replace(old_word, new_word)

# Save the modified DataFrame back to the CSV file
#df_filled.to_csv('./Tower_Sentiment_New.xlsx', index=False)

#Removing all mistakes from the dataset where names were not spelt right
specific_word = 'Neural'
df_filled = df_filled[~df_filled['Sentiment'].str.contains(specific_word, case=False)]
specific_word = 'Positve'
df_filled = df_filled[~df_filled['Sentiment'].str.contains(specific_word, case=False)]
print(len(df_filled))
df_filled.head()

#loading data to process
data = [df_filled['Text'][0]]
for i in range (1,len(df_filled)):
    data = data + [df_filled['Text'][i]]
print(data)

#setting up sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")
specific_model1 = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
specific_model2 = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

#processing the data
output = sentiment_pipeline(data)
output2 = specific_model1(data)
output3 = specific_model2(data)

print(output)
print(output2)
print(output3)

sentiment = []
score = []

for i in range (1,10):
    data = df_filled['Text'][i]
    output = specific_model1(data)
    sentiment = sentiment + [output[0]["label"]]
    score = score +[output[0]["score"]]
print(sentiment)
print(score)

sentiment_data = []

for i in range (1,10):
  sentiment_new = df_filled["Sentiment"][i]
  sentiment_data.append(sentiment_new)

print(sentiment_data)

sentiment_data_upper = list((map(lambda x: x.lower(), sentiment_data)))


print(sentiment)
print(sentiment_data_upper)

total = []

for i in range (len(sentiment)):
  j = sentiment[i]
  k = sentiment_data_upper[i]
  if j == k:
    print("true")
    total.append(1)
  else:
    print("false")
    total.append(0)

print(total)

count = 0
for i in range (len(total)):
  t = total[i]
  if t == 1:
    count += 1

print(count)
accuracy = (count / len(total)) * 100
print(accuracy)

#testing purposes only on how to add to array, dont run this node
data = [df_filled['Text'][0]]
data2 = [df_filled['Text'][1]]
data3 = data + data2
data4 = ["I", "Yes"]
print(data3)
print(data4)

#checking output example , dont use this
print(output[0]["label"])
print(output[0]["score"])
print(len(output))
print(output)

#dont use this
data = df_filled['Text'][4]
print(data)

# Dont use after this
#Load data
df = pd.read_excel('.\Tower_Sentiment.xlsx', 'TOWER REAL') #try replacing this with excel file ???
df.shape

# Checking for missing values
df.isnull().sum()

df.drop(['ID', 'Timestamp', 'Dim Milestone - Dim Milestone Milestone → Description', 'Dim Milestone - Dim Milestone Milestone → Name'], axis=1)

