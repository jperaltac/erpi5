#
# This file is part of the erpi5 project and is licensed under the
# GNU General Public License v3.  See the LICENSE file for details.
#
from tensorflow.keras import layers, Sequential

model = Sequential([
    layers.Dense(1, activation='relu',
                 input_shape=(5,))
    ])

