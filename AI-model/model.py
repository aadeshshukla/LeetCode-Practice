import tensorflow as tf
import numpy as np

# 1. Data (Inputs and Outputs)
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# 2. Define the Architecture
# 'Dense' means every neuron is connected to every neuron in the next layer.
# We are using 1 layer with 1 neuron.
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# 3. Compile the Model
# 'Optimizer' is the logic to improve the guess.
# 'Loss' is how the model measures how wrong it is.
model.compile(optimizer='sgd', loss='mean_squared_error')

# 4. Train the Model (The "Epochs" are training loops)
print("Starting training...")
model.fit(xs, ys, epochs=500, verbose=0) 

# 5. Predict
print("Finished. Predicting value for 10.0...")
print(model.predict(np.array([10.0])))