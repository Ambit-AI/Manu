# -*- coding: utf-8 -*-
"""AmbitProject3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/124tv7Ricw0d2Go0tiia1O8hknh-Vqj1v
"""

import pandas as pd
import numpy as np

df2 = pd.read_csv('/content/drive/MyDrive/Tower_Sentiment.csv')
#Dropping columns that do not need to be read
df2.drop(df2.columns[[4,5,6,7,8]], axis=1, inplace=True)
df2.head()

df2['Text'] = df2['Text'].fillna('')
grouped_df = df2.groupby('Conversation ID').agg({'Text': '. '.join, 'FullSentiment': 'first'}).reset_index()
grouped_df.head()
#len(grouped_df)

df2['Text'] = df2['Text'].fillna('')

# Filter out rows where the 'Source' column is 'bot'
df2 = df2.drop(df2[df2['Source'] == 'bot'].index)

# Group by 'ID' and concatenate the 'Text' for each group separated by a period ('.')
grouped_df = df2.groupby('Conversation ID').agg({'Text': '. '.join, 'FullSentiment': 'first'}).reset_index()

# Print the first few rows of the grouped DataFrame
print(grouped_df.head())

text_paragraph = grouped_df['Text'][5]
print(text_paragraph)

df_filled = grouped_df.fillna(" ")
old_word = 'Neural'
new_word = 'Neutral'
# Find rows containing the target word and replace it with the new word
df_filled['FullSentiment'] = df_filled['FullSentiment'].replace(old_word, new_word)

old_word = 'Positve'
new_word = 'Positive'
# Find rows containing the target word and replace it with the new word
df_filled['FullSentiment'] = df_filled['FullSentiment'].replace(old_word, new_word)

old_word = 'positive'
new_word = 'Positive'
# Find rows containing the target word and replace it with the new word
df_filled['FullSentiment'] = df_filled['FullSentiment'].replace(old_word, new_word)

# Save the modified DataFrame back to the CSV file
df_filled.to_csv('/content/drive/MyDrive/Tower_Sentiment_New.csv', index=False)

#Removing all mistakes from the dataset where names were not spelt right
specific_word = 'Neural'
df_filled = df_filled[~df_filled['FullSentiment'].str.contains(specific_word, case=False)]
specific_word = 'Positve'
df_filled = df_filled[~df_filled['FullSentiment'].str.contains(specific_word, case=False)]
print(len(df_filled))
df_filled.head()

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
#train and test data split
train_data, test_data = train_test_split(df_filled, test_size=0.3, random_state=42)

vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust max_features as needed

# Fit and transform the vectorizer on the training data
X_train = vectorizer.fit_transform(train_data['Text'])
y_train = train_data['FullSentiment']

# Transform the vectorizer on the test data
X_test = vectorizer.transform(test_data['Text'])
y_test = test_data['FullSentiment']

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

#LinearRegression
linearR = LinearRegression()
#Create a Naive Bayes classifier
classifier = MultinomialNB()
#LogisticRegression
logistic = LogisticRegression()
#Decision Tree
decision = DecisionTreeClassifier()
#Random forest
forest = RandomForestClassifier()
#SVM
svm = SVC()

# Train the classifier on the training data
#linearR.fit(X_train, y_train)
classifier.fit(X_train, y_train)
logistic.fit(X_train, y_train)
decision.fit(X_train, y_train)
forest.fit(X_train, y_train)
svm.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report

# Predict on the test data
y_pred = classifier.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Naive Bayes:", accuracy)

# l_pred = linearR.predict(X_test)
# # Calculate accuracy
# accuracy = accuracy_score(y_test, l_pred)
# print("Linear Regression:", accuracy)

logistic_pred = logistic.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, logistic_pred)
print("Logistic Regression:", accuracy)

d_pred = decision.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, d_pred)
print("Decision Tree:", accuracy)

f_pred = forest.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, f_pred)
print("Random Forest:", accuracy)

svm_pred = svm.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, svm_pred)
print("Svm:", accuracy)

# Generate a classification report
print("Naive Bayes Report:")
print(classification_report(y_test, y_pred))

print("Logistic Regression Report:")
print(classification_report(y_test, logistic_pred))

print("Decision Tree Report:")
print(classification_report(y_test, d_pred))

print("Random Forest Report:")
print(classification_report(y_test, f_pred))

print("SVM Report:")
print(classification_report(y_test, svm_pred))

new_text = "no"
new_text_features = vectorizer.transform([new_text])

#Bayes
predicted_sentiment = classifier.predict(new_text_features)[0]
print("Predicted Sentiment Bayes:", predicted_sentiment)
#logistic
predicted_sentiment = logistic.predict(new_text_features)[0]
print("Predicted Sentiment logistic:", predicted_sentiment)
#Decision treee
predicted_sentiment = decision.predict(new_text_features)[0]
print("Predicted Sentiment Decision tree:", predicted_sentiment)
#Forest
predicted_sentiment = forest.predict(new_text_features)[0]
print("Predicted Sentiment forest:", predicted_sentiment)
#Svm
predicted_sentiment = svm.predict(new_text_features)[0]
print("Predicted Sentiment Svm:", predicted_sentiment)