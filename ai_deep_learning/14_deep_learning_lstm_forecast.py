import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

ticker = "RELIANCE.NS"
data = yf.download(ticker, start="2015-01-01", end="2024-01-01")['Close'].values.reshape(-1, 1)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

def create_sequences(data, time_step=60):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

X, y = create_sequences(scaled_data)
X = X.reshape(X.shape[0], X.shape[1], 1)

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(Dropout(0.2)) 
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(units=1)) 

model.compile(optimizer='adam', loss='mean_squared_error')

print("🧠 TRAINING NEURAL NETWORK (This simulates a GPU cluster)...")
model.fit(X, y, epochs=1, batch_size=32, verbose=1) 

predicted_price = model.predict(X[-1].reshape(1, 60, 1))
real_prediction = scaler.inverse_transform(predicted_price)

print(f"--- AI PREDICTION ---")
print(f"Based on the last 60 days, the AI predicts next price: ₹{real_prediction[0][0]:.2f}")