import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU

def build_generator(latent_dim, output_dim):
    model = Sequential()
    model.add(Dense(32, input_dim=latent_dim))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(output_dim, activation='linear')) 
    return model

def build_discriminator(input_dim):
    model = Sequential()
    model.add(Dense(32, input_dim=input_dim))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(1, activation='sigmoid')) 
    return model

latent_dim = 5
data_dim = 1 
generator = build_generator(latent_dim, data_dim)
discriminator = build_discriminator(data_dim)
discriminator.compile(loss='binary_crossentropy', optimizer='adam')

discriminator.trainable = False
gan = Sequential([generator, discriminator])
gan.compile(loss='binary_crossentropy', optimizer='adam')

print("🧠 TRAINING GAN TO FAKE MARKET DATA...")
real_data = np.random.normal(0, 0.01, (1000, 1))

for epoch in range(500): 
    noise = np.random.normal(0, 1, (1000, latent_dim))
    fake_data = generator.predict(noise, verbose=0)
    
    x_combined = np.concatenate([real_data, fake_data])
    y_combined = np.concatenate([np.ones((1000, 1)), np.zeros((1000, 1))])
    
    d_loss = discriminator.train_on_batch(x_combined, y_combined)
    
    noise = np.random.normal(0, 1, (1000, latent_dim))
    y_mislabeled = np.ones((1000, 1)) 
    g_loss = gan.train_on_batch(noise, y_mislabeled)

synthetic_scenario = generator.predict(np.random.normal(0, 1, (10, latent_dim)))
print(f"--- SYNTHETIC MARKET DATA (Returns) ---")
print(synthetic_scenario.flatten())
print("Insight: This data never existed, but it LOOKS mathematically real.")