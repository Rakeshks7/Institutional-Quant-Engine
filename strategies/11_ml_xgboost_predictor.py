import yfinance as yf
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = yf.download("HDFCBANK.NS", start="2020-01-01", end="2024-01-01")
df = pd.DataFrame()
df['Close'] = data['Close']

df['Returns'] = df['Close'].pct_change()
df['Vol_5'] = df['Returns'].rolling(5).std()
df['Mom_5'] = df['Close'].pct_change(5)
df = df.dropna()

df['Target'] = np.where(df['Returns'].shift(-1) > 0, 1, 0)
df = df.dropna()

features = ['Returns', 'Vol_5', 'Mom_5']
X = df[features]
y = df['Target']

split = int(len(X) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = XGBClassifier(n_estimators=100, learning_rate=0.05, use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"--- ML MODEL REPORT (XGBoost) ---")
print(f"Model Accuracy: {accuracy*100:.2f}%")
print("Feature Importance:")
for name, score in zip(features, model.feature_importances_):
    print(f"   {name}: {score:.4f}")