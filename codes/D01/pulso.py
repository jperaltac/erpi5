#
# This file is part of the erpi5 project and is licensed under the
# GNU General Public License v3.  See the LICENSE file for details.
#
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
signal = (t % 0.2 < 0.05).astype(float)

plt.plot(t, signal)
plt.title("Pulso de estimulación")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.ylim(-0.2, 1.2)
plt.grid()
plt.show()
