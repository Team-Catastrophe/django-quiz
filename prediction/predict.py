import numpy as np
import pandas as pd

def predict_result(X_test):
    # Importing the dataset
    dataset = pd.read_csv('user.csv')
    X = dataset.iloc[:, 0].values
    y = dataset.iloc[:, 1].values

    # Encoding categorical data
    # Encoding the Independent Variable
    from sklearn.preprocessing import LabelEncoder
    labelencoder_X = LabelEncoder()
    X = labelencoder_X.fit_transform(X)
    # Encoding the Dependent Variable
    labelencoder_y = LabelEncoder()
    y = labelencoder_y.fit_transform(y)

    # Fitting Logistic Regression to the Training set
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X.reshape(-1, 1), y.reshape(-1, 1))

    y_pred = classifier.predict(X_test)

    return y_pred
