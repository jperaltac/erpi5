#!/usr/bin/env python3
#
# This file is part of the erpi5 project and is licensed under the
# GNU General Public License v3.  See the LICENSE file for details.
#
# gflops_pi5.py  –  calcula GFLOPS sencillos en una Raspberry Pi 5
import time, numpy as np

N = 1024*12                     # tamaño de la matriz (ajusta según tu RAM)
dtype = np.float32           # usa float32 para no exigir FPU doble precisión

# Matrices aleatorias
A = np.random.rand(N, N).astype(dtype)
B = np.random.rand(N, N).astype(dtype)

# Calentamiento ligero (evita primer efecto JIT/alloc)
np.dot(A[:32, :32], B[:32, :32])

# Medición
t0 = time.perf_counter()
C = np.dot(A, B)
elapsed = time.perf_counter() - t0

# Cálculo de FLOPS
flops = 2 * N**3
gflops = flops / elapsed / 1e9

print(f"Tamaño: {N}×{N}")
print(f"Tiempo : {elapsed:.3f} s")
print(f"Rendim.: {gflops:.2f} GFLOPS")

