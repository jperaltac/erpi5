from tensorflow.keras import layers, Sequential

model = Sequential([
    layers.Dense(1, activation='relu',
                 input_shape=(5,))
    ])

