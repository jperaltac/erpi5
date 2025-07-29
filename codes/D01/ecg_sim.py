#
# This file is part of the erpi5 project and is licensed under the
# GNU General Public License v3.  See the LICENSE file for details.
#
import numpy as np
import matplotlib.pyplot as plt

# Tiempo
t = np.linspace(0, 1, 500)

# Simulación muy básica de una señal ECG
ecg = np.sin(2 * np.pi * 5 * t) * np.exp(-5 * t)
ecg += np.random.normal(0, 0.05, size=t.shape)

# Mostrar
plt.plot(t, ecg, label="ECG simulado")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.title("Señal ECG Simulada")
plt.legend()
plt.grid()
plt.show()
