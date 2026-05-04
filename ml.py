import pandas as pd
from sklearn.ensemble import IsolationForest


def train_model():

    data = {
        "amount": [100, 200, 300, 500, 700, 1000, 2000]
    }

    df = pd.DataFrame(data)

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    model.fit(df)

    return model


model = train_model()

def predict_fraud(amount):

    prediction = model.predict([[amount]])

    return prediction[0]