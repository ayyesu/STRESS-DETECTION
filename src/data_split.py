from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import numpy as np

def model(data):
    x = np.array(data["text"])
    y = np.array(data["label"])

    cv = CountVectorizer()
    X = cv.fit_transform(x)
    xtrain, xtest, ytrain, ytest = train_test_split(X, y,
                                                    test_size=0.33,
                                                    random_state=42)
    model = BernoulliNB()
    model.fit(xtrain, ytrain)
    user = input("Enter a Text: ")
    data = cv.transform([user]).toarray()
    output = model.predict(data)
    print(output)
