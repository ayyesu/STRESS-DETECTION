from src import config
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# DATASET
df = config.DATASET

def wordcloudplt(data):
    text = " ".join(i for i in data.text)
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords,
                        background_color="white").generate(text)
    plt.figure( figsize=(15,10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
