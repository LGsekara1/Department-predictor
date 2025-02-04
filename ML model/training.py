import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from keras.models import Sequential
from keras.layers import Dense,Dropout,BatchNormalization
from keras.optimizers import Adam
from keras.utils import plot_model
import tensorflow as tf

# Load data
df = pd.read_csv("data.csv")
print("Data is loaded!")
# Features and target
X = df[["GPA", "Rank"]]
Y = df["Department"]

# Encode the target
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(Y)
y_one_hot = pd.get_dummies(y_encoded).values

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_one_hot, test_size=0.2, random_state=42)
print("Data is split and ready")
# Build model

model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    BatchNormalization(),#Used to normalize the input layer by re-centering and re-scaling
    Dropout(0.5),#Used to drop certain neurons in training not to heaviliy rely on any neuron
    Dense(32, activation='relu'),
    BatchNormalization(),
    Dense(y_train.shape[1], activation='softmax')
])


# Compile and train model
model.compile(optimizer=Adam(learning_rate=0.001), loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=1)

# Save model, scaler, and encoder
model.save('department_allocation_model.h5')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(encoder, 'label_encoder.pkl')

print("Model, scaler, and encoder saved successfully. THe model is good to go !")
