# -*- coding: utf-8 -*-
"""openai.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pIpTF1pG1084LBtK_qAuYkGNmUJNulN3
"""

pip install openai

import pandas as pd

# Read the CSV file and skip the first row
df2 = pd.read_csv('/content/drive/MyDrive/Tower_Sentiment.csv', skiprows=0)

# Drop columns that do not need to be read
df2.drop(df2.columns[[4, 5]], axis=1, inplace=True)
df2.head()

import pandas as pd

# Assuming your dataframe 'df2' and grouping logic as provided

# Group by 'Conversation ID' and aggregate 'Text' and 'FullSentiment'
def concatenate_text_and_sentiment(group):
    combined_text = ', '.join([f"{source.capitalize()}: {text}" for _, source, text in group[['Timestamp', 'Source', 'Text']].itertuples(index=False)])
    full_sentiment = group['FullSentiment'].iloc[0]  # Get FullSentiment from the first row of the group
    return pd.Series({
        'Conversation ID': group['Conversation ID'].iloc[0],
        'Combined_Text': combined_text,
        'FullSentiment': full_sentiment
    })

grouped_df = df2.groupby('Conversation ID').apply(concatenate_text_and_sentiment).reset_index(drop=True)

#FOR NOW
grouped_df.dropna(subset=['FullSentiment'], inplace=True)

print(grouped_df)

import random
# Get the number of rows in the DataFrame
num_rows = len(grouped_df)

# Generate a random index within the valid range
random_index = random.randint(0, num_rows - 1)

# Get the text paragraph at the random index
text_paragraph = grouped_df['Combined_Text'][random_index]
sentiment = grouped_df['FullSentiment'][random_index]
conversation_ID = grouped_df['Conversation ID'][random_index]

print(conversation_ID)
print(text_paragraph)
print(sentiment)

import os
import openai

#do not use without consulting please
openai.api_key = "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"
system_message = "You will be provided with text or conversation from a chat bot dataset, and your task is to analyze the sentiment of the users' interactions."

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system","content": system_message},
    {"role": "user","content": text_paragraph}
  ],
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

output_content = response['choices'][0]['message']['content']

print("Text:")
print(text_paragraph)
print()
print("Sentiment:",output_content)
print("Annotated Sentiment: ", sentiment)