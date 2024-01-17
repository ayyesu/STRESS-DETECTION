import pandas as pd
import numpy as np
from src import config
from src import word_cloud
from src import data_split

# Natural Language toolkit
import nltk
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
stopword=set(stopwords.words('english'))

# Regular Expression
import re

df = pd.read_csv(config.DATASET)
def feature_processing(data: pd.DataFrame):

    print(df.head())

    # Checking for null values
    print(df.isnull().sum())



feature_processing(df)

def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text
df["text"] = df["text"].apply(clean)


# visualizing a word cloud of the text column
word_cloud.wordcloudplt(df)

# Marking labels with 0(as No Stress) and 1(as Stress)
df["label"] = df["label"].map({0: "No Stress", 1: "Stress"})
data = df[["text", "label"]]
print(data.head())


data_split.model(df)
